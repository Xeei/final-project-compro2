import pygame as pg
from config import Config, GameState
from game_card import Deck
from game_menu import GameMenu
from game_ui import GameUI

class GameRunner:



    def __init__(self):
        pg.init()
        pg.display.set_caption("Black Jackkkkkkkkkkk")
        self.__screen = pg.display.set_mode(Config.screen_size)
        self.__screen.fill("white")

        self.__clock = pg.time.Clock()
        self.__running = True
        self.__game_menu = GameMenu(self.__screen)
        self.__game_ui = GameUI(self.__screen)
        self.__game_state = GameState.MENU

    def __render(self):
        if self.__game_state == GameState.MENU:
            self.__game_menu.render()
        elif self.__game_state == GameState.INGAME:
            self.__game_ui.render()
        pg.display.update()

    def __handle_ingame_event(self, event):
        if event.type == pg.KEYDOWN:
            self.__game_ui.onKeyDown(event.key)

    def __handle_menu_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            print(f"Click CLick at : {pos}")
            name_butt = self.__game_menu.onClick(pos)
            if name_butt == "PLAY":
                self.__game_state = GameState.INGAME
                self.__game_ui.init_game()

    def __handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__running = False
            if self.__game_state == GameState.MENU:
                self.__handle_menu_event(event)
            elif self.__game_state == GameState.INGAME:
                self.__handle_ingame_event(event)

    def game_loop(self):
        while self.__running:
            self.__handle_events()
            self.__render()
            self.__clock.tick(60)

        pg.quit()

if __name__ == "__main__":
    g = GameRunner()
    g.game_loop()

