from multiprocessing import Process
import tkinter as tk
from game_runner import GameRunner
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from game_db import GameDb
import seaborn as sns
from datetime import datetime
import pandas as pd


# prevent pickleable
def run_game():
    g = GameRunner()
    g.game_loop()


def New_page():
    db = GameDb()
    popup = tk.Toplevel()
    popup.title("Data visualization")
    popup.geometry("1000x500")
    popup.grab_set()

    tab_parent = ttk.Notebook(popup)

    # * TAB PLAYER SCORE FREQUENCY
    player_score_fraquency_tab = ttk.Frame(tab_parent)
    player_score_fraquency = db.player_score_fraquency()
    fig, ax = plt.subplots()
    player_score_fraquency["player_score"].hist(
        ax=ax, figsize=(10, 20), color="#A8E6CF"
    )
    ax.set_xlabel("Player Score")
    ax.set_ylabel("Frequency")
    ax.set_title("Score Frequency")
    ax.grid(False)

    canvas = FigureCanvasTkAgg(fig, master=player_score_fraquency_tab)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    tab_parent.add(player_score_fraquency_tab, text="Score Fraquency")

    # * TAB PLAYER WIN/LOSE/TIE POPORTION (RESULT POPORTION)
    player_summary_result_tab = ttk.Frame(tab_parent)
    player_summary_result = db.player_summary_result()
    player_summary_result.set_index("result", inplace=True)
    fig, ax = plt.subplots()
    color_map = {
        "win": "#A8E6CF",  # pastel green
        "lost": "#FF8C94",  # pastel red/pink
        "tie": "#D3D3D3",  # light gray
    }
    colors = [
        color_map.get(result, "#AEDFF7") for result in player_summary_result.index
    ]
    slices, texts, numbers = ax.pie(
        player_summary_result["number"],
        colors=colors,
        autopct="%1.2f%%",
        textprops={"color": "w"},
    )
    fig.set_size_inches((10, 20))
    ax.legend(
        slices, player_summary_result.index, title="Legend", bbox_to_anchor=(1, 1)
    )
    ax.set_title("Result Poportion")

    canvas = FigureCanvasTkAgg(fig, master=player_summary_result_tab)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    tab_parent.add(player_summary_result_tab, text="Player Win/Lost/Tie ")

    # * SCATTER PLOT RELATION BETWEEN SCORE AND TIME USE
    relation_tab = ttk.Frame(tab_parent)

    player_games = db.player_games()
    temp_data = []
    for i, player_game in player_games.iterrows():
        game_events = db.player_game_events_by_game_id(
            game_id=player_game.get("game_id")
        )
        for j, ev in game_events.iterrows():
            if j == 0:
                prev_time = datetime.strptime(
                    player_game.get("start_time"), "%Y-%m-%d %H:%M:%S.%f"
                )
            else:
                prev_time = datetime.strptime(
                    game_events.iloc[j - 1].get("time"), "%Y-%m-%d %H:%M:%S.%f"
                )

            time_use = (
                datetime.strptime(ev.get("time"), "%Y-%m-%d %H:%M:%S.%f") - prev_time
            )
            time_user_seconds = time_use.total_seconds()
            pct_of_score = (ev.get("before_score") / 21) * 100

            temp_data.append(
                [ev.get("name"), ev.get("time"), time_user_seconds, pct_of_score]
            )
        # print("-"*30)

    np_data = np.array(temp_data)

    df = pd.DataFrame(np_data, columns=["name", "time", "time_use", "pct_of_score"])
    df["time_use"] = df["time_use"].astype(float)
    df["pct_of_score"] = df["pct_of_score"].astype(float)

    color_pair_palette = {
        "stand": "#A8E6CF",  # pastel green
        "hit": "#FF8C94",  # pastel red/pink
    }
    relation_plot = sns.pairplot(
        df,
        vars=["time_use", "pct_of_score"],
        hue="name",
        markers=["o", "D"],
        palette=color_pair_palette,
    )

    relation_plot.figure.set_size_inches((10, 20))

    canvas = FigureCanvasTkAgg(relation_plot.figure, master=relation_tab)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    tab_parent.add(relation_tab, text="RELATION BETWEEN SCORE AND TIME USE")

    table_tab = ttk.Frame(tab_parent)

    table_columns = ["order"] + player_games.columns.tolist()
    table_data = player_games.iterrows()
    tree = ttk.Treeview(table_tab, columns=table_columns, show="headings")
    cols_size = {
        "order": 5,
        "game_id": 250,
        "player_score": 15,
        "dealer_score": 15,
        "result": 15,
    }
    cols_align = {"game_id": "w", "player_score": "w", "dealer_score": "w"}
    for col in table_columns:
        tree.heading(col, text=col)
        tree.column(
            col, width=cols_size.get(col, 100), anchor=cols_align.get(col, "center")
        )

    for _, row in table_data:
        tree.insert("", tk.END, values=[_] + row.tolist())
    tree.pack(fill="both", expand=True)

    tab_parent.add(table_tab, text="TABLE")

    tab_parent.pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blackjack Menu")
        self.geometry("300x125")

        self.label = tk.Label(self, text="Welcome to my Blackjack game")
        self.label.pack()

        self.start_button = tk.Button(
            self, text="Start Game", command=self.open_game_window
        )
        self.start_button.pack()

        self.data_button = tk.Button(self, text="Data", command=New_page)
        self.data_button.pack()

        self.exit_button = tk.Button(self, text="Exit", command=self.exit)
        self.exit_button.pack()

        self.protocol("WM_DELETE_WINDOW", self.exit)

    def exit(self):
        plt.close("all")
        self.destroy()

    def open_game_window(self):
        p = Process(target=run_game)
        p.start()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
