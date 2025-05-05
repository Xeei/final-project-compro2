from multiprocessing import Process
import tkinter as tk
from game_runner import GameRunner

def run_game():
    g = GameRunner()
    g.game_loop()

def open_game_window():
    p = Process(target=run_game)
    p.start()

def launch_menu():
    root = tk.Tk()
    root.title("Blackjack Menu")
    root.geometry("300x200")

    start_button = tk.Button(root, text="Start Game", command=open_game_window)
    start_button.pack(pady=20)

    start_button = tk.Button(root, text="Data", command=open_game_window)
    start_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    launch_menu()