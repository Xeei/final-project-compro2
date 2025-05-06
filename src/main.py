from multiprocessing import Process
import tkinter as tk
from game_runner import GameRunner

# prevent pickleable
def run_game():
    g = GameRunner()
    g.game_loop()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blackjack Menu")
        self.geometry("300x125")

        self.label = tk.Label(self, text="Welcome to my Blackjack game")
        self.label.pack()

        self.start_button = tk.Button(self, text="Start Game", command=self.open_game_window)
        self.start_button.pack()

        self.data_button = tk.Button(self, text="Data", command=lambda: print("hello"))
        self.data_button.pack()

        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.pack()

    def open_game_window(self):
        p = Process(target=run_game)
        p.start()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()