import pygame
from config import Config
from card import Deck

class GameRunner:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Black Jackkkkkkkkkkk")
        self.__screen = pygame.display.set_mode(Config.screen_size)
        self.__screen.fill("white")

        self.__clock = pygame.time.Clock()
        self.__running = True
        self.__deck = Deck()

    def __start_game(self):
        pass

    def __game_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False


        # game render

        pygame.display.update()
        self.__clock.tick(60)

    def run(self):
        self.__start_game()
        self.__deck.display_all_card(self.__screen)

        while self.__running:
            self.__game_update()
        pygame.quit()

if __name__ == "__main__":
    g = GameRunner()
    g.run()

