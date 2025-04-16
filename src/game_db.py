import pandas as pd
import sqlite3 as sql
from threading import Lock

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
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            genre TEXT,
            release_year INTEGER
        );
        """
        try:
            self.__cursor.execute(query)
            self.__db.commit()
            print("Table 'games' created successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")

    def read_db(self, query: str):
        try:
            return pd.read_sql_query(query, self.__db)
        except Exception as e:
            print(f"Error reading database: {e}")
            return None

    def close(self):
        if self.__db:
            self.__db.close()

db_instance = GameDb()
db_instance.create_table()

df = db_instance.read_db("SELECT * FROM games")
print(df)

db_instance.close()