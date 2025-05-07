import pandas as pd
import matplotlib.pyplot as plt
from game_db import GameDb
import seaborn as sns
from datetime import datetime
import numpy as np

db = GameDb()

player_games = db.player_games()
temp_data = []
for i, player_game in player_games.iterrows():
    print("="*30)
    # print(i, player_game.get("game_id"), f"start at: {player_game.get("start_time")}")
    game_events = db.player_game_events_by_game_id(game_id=player_game.get("game_id"))
    print("-"*30)
    # print(game_events.head())
    for j, ev in game_events.iterrows():
        if j == 0:
            prev_time = datetime.strptime(player_game.get("start_time"), "%Y-%m-%d %H:%M:%S.%f")
        else:
            prev_time = datetime.strptime(game_events.iloc[j-1].get("time"), "%Y-%m-%d %H:%M:%S.%f")

        time_use = datetime.strptime(ev.get("time"), "%Y-%m-%d %H:%M:%S.%f") - prev_time
        time_user_seconds = time_use.total_seconds()
        # print(ev.get("name"), ev.get("time"), time_use.total_seconds(), ev.get("before_score"))
        pct_of_score = (ev.get("before_score")/21)*100

        temp_data.append([ev.get("name"), ev.get("time"), time_user_seconds, pct_of_score])
    print("-"*30)

np_data = np.array(temp_data)

df = pd.DataFrame(np_data, columns=["name", "time", "time_use", "pct_of_score"])
df["time_use"] = df["time_use"].astype(float)
df["pct_of_score"] = df["pct_of_score"].astype(float)
print(df.head())

sns.pairplot(df, vars = ["time_use", "pct_of_score"], hue="name", markers=["o", "D"])
plt.show()