import pandas as pd
import sqlite3 as sql
from threading import Lock
import uuid


class GameDb:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(GameDb, cls).__new__(cls)
                cls._instance.__init_db()
        return cls._instance

    def __init_db(self):
        self.__db = sql.connect("db/db.db")
        self.__cursor = self.__db.cursor()

    def create_table(self):
        query = """
            create table games
            (
                game_id      TEXT not null
                    primary key,
                start_time   DATETIME,
                end_time     DATETIME,
                player_score INTEGER,
                dealer_score INTEGER,
                result       TEXT(10)
            );

            create table games_events
            (
                game_id      INTEGER
                    references games,
                name         TEXT(10),
                card_symbol  TEXT(1),
                card_number  TEXT(2),
                time         DATETIME,
                before_score INTEGER,
                after_score  INTEGER
            );
            """
        try:
            self.__cursor.execute(query)
            self.__db.commit()
            print("Table 'games' created successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")

    def insert_game(self, start_time, end_time, player_score, dealer_score, result):
        query = """
        INSERT INTO games (game_id, start_time, end_time,
        player_score, dealer_score, result)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        game_id = str(uuid.uuid4())

        try:
            self.__cursor.execute(
                query,
                (game_id, start_time, end_time, player_score, dealer_score, result),
            )
            self.__db.commit()
            print(f"Game inserted with ID: {game_id}")
            return game_id
        except Exception as e:
            print(f"Error inserting game: {e}")
            return None

    def insert_game_events(self, game_id, events: list):
        query = """
        insert into games_events (
        game_id, name, card_symbol,
        card_number, "time", before_score, after_score
        )
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """

        try:

            for ev in events:
                if ev.name == "stand":
                    self.__cursor.execute(
                        query,
                        (
                            game_id,
                            ev.name,
                            None,
                            None,
                            ev.time,
                            ev.before_score,
                            ev.after_score,
                        ),
                    )
                elif ev.name == "hit":
                    self.__cursor.execute(
                        query,
                        (
                            game_id,
                            ev.name,
                            ev.card.symbol,
                            ev.card.number,
                            ev.time,
                            ev.before_score,
                            ev.after_score,
                        ),
                    )
                else:
                    raise ValueError("Invalid ev.name")
            self.__db.commit()
            print(f"Game inserted with ID: {game_id}")
            return game_id
        except Exception as e:
            print(f"Error inserting game: {e}")
            return None

    def player_score_fraquency(self) -> pd.DataFrame:
        try:
            query = """
            select player_score
            from games
            order by player_score
            """
            df = pd.read_sql_query(query, self.__db)
            return df
        except Exception as e:
            print(f"Error reading player_score_fraquency : {e}")
            return pd.DataFrame({})

    def player_summary_result(self) -> pd.DataFrame:
        try:
            query = """
            select result, count(result) as number
            from games
            group by result
            """
            df = pd.read_sql_query(query, self.__db)
            return df
        except Exception as e:
            print(f"Error reading player_summary_result : {e}")
            return pd.DataFrame({})

    def player_games(self):
        try:
            query = """
            select *
            from games
            """
            df = pd.read_sql_query(query, self.__db)
            return df
        except Exception as e:
            print(f"Error reading player_games : {e}")
            return pd.DataFrame({})

    def player_game_events_by_game_id(self, game_id):
        try:
            query = f"""
            select *
            from games_events
            where game_id = '{game_id}'
            """
            df = pd.read_sql_query(query, self.__db)
            return df
        except Exception as e:
            print(f"Error reading player_games : {e}")
            return pd.DataFrame({})

    def read_db(self, query: str):
        try:
            return pd.read_sql_query(query, self.__db)
        except Exception as e:
            print(f"Error reading database: {e}")
            return None

    def close(self):
        if self.__db:
            self.__db.close()
