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
        self.__db = sql.connect('db/db.db')
        self.__cursor = self.__db.cursor()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS games
        (
            game_id      TEXT not null
                primary key,
            start_time   DATETIME,
            end_time     DATETIME,
            player_score INTEGER,
            dealer_score INTEGER
        );

        CREATE TABLE IF NOT EXISTS game_hand
        (
            game_id     INTEGER
                references games,
            card_symbol TEXT(1),
            action      TEXT(5),
            deal_at     DATETIME,
            card_number TEXT(2),
            time_use    integer
        );
        """
        try:
            self.__cursor.execute(query)
            self.__db.commit()
            print("Table 'games' created successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")

    def insert_game(self, start_time, end_time, player_score, dealer_score):
        query = """
        INSERT INTO games (game_id, start_time, end_time, player_score, dealer_score)
        VALUES (?, ?, ?, ?, ?);
        """
        game_id = str(uuid.uuid4())

        try:
            self.__cursor.execute(query, (game_id, start_time, end_time, player_score, dealer_score))
            self.__db.commit()
            print(f"Game inserted with ID: {game_id}")
            return game_id
        except Exception as e:
            print(f"Error inserting game: {e}")
            return None
        
    def insert_game_events(self, game_id, events: list):
        query = """
        insert into games_events (game_id, name, card_symbol, card_number, "time", before_score, after_score)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """

        try:

            for ev in events:
                if ev.name == "stand":
                    self.__cursor.execute(query, (game_id, ev.name, None, None, 
                                                ev.time, ev.before_score, ev.after_score))
                elif ev.name == "hit":
                    self.__cursor.execute(query, (game_id, ev.name, ev.card.symbol, ev.card.number, 
                            ev.time, ev.before_score, ev.after_score))
                else:
                    raise ValueError("Invalid ev.name")
            self.__db.commit()
            print(f"Game inserted with ID: {game_id}")
            return game_id
        except Exception as e:
            print(f"Error inserting game: {e}")
            return None


    def read_db(self, query: str):
        try:
            return pd.read_sql_query(query, self.__db)
        except Exception as e:
            print(f"Error reading database: {e}")
            return None

    def close(self):
        if self.__db:
            self.__db.close()