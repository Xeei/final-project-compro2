from datetime import datetime
from src.game_db import GameDb
db = GameDb()

# insert a game record
game_id = db.insert_game(
    start_time=datetime.now(),
    end_time=datetime.now(),
    player_score=21,
    dealer_score=18
)

# optional: view inserted data
print(db.read_db("SELECT * FROM games"))

# close db when done
db.close()
