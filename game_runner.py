import pygame
from config import Config
from game_card import Deck
from game_menu import GameMenu
from game_ui import GameUI

class GameRunner:



    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Black Jackkkkkkkkkkk")
        self.__screen = pygame.display.set_mode(Config.screen_size)
        self.__screen.fill("white")

        self.__clock = pygame.time.Clock()
        self.__running = True
        self.__game_menu = GameMenu()
        self.__game_ui = GameUI()
        self.__status = "MENU"
        # * status -> MENU, INGAME

    def __init_game(self):
        self.__deck = Deck()

    def __start_game(self):
        self.__screen.fill(Config.BG_COLOR)
        self.__game_menu.render(self.__screen)

    def __game_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(f"Click CLick at : {pos}")
                if self.__status == "MENU":
                    name_butt = self.__game_menu.onClick(pos)
                    if name_butt == "PLAY":
                        self.__game_ui.render(self.__screen)
                        self.__status = "INGAME"
                        self.__init_game()
                elif self.__status == "INGAME":
                    pass
        # game render

        pygame.display.update()
        self.__clock.tick(60)

    def run(self):
        self.__start_game()
        # self.__deck.display_all_card(self.__screen)

        while self.__running:
            self.__game_update()
        pygame.quit()

if __name__ == "__main__":
    g = GameRunner()
    g.run()

