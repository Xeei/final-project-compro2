import pandas as pd
import matplotlib.pyplot as plt
from game_db import GameDb

db = GameDb()

player_score_fraquency = db.player_score_fraquency()
# Disable binning by setting bins to unique values
# plt.figure(figsize=(8, 6))
# df['col1'].hist()
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram without Binning')
# plt.grid(False)

player_score_fraquency['player_score'].hist()
plt.grid(False)
plt.show()