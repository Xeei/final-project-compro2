import pygame
from config import Config

class GameRunner:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(Config.screen_size)
        self.__clock = pygame.time.Clock()
        self.__running = True

    def run(self):
        while self.__running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

            self.__screen.fill("purple")

            # RENDER YOUR GAME HERE

            pygame.display.flip()

            self.__clock.tick(60)  # limits FPS to 60
        pygame.quit()

if __name__ == "__main__":
    g = GameRunner()
    g.run()

