import pygame as pg
from config import Config
class StartUI:
    def __init__(self):
        self.__head_size = (600, 160)
        self.__head_image = pg.transform.smoothscale(pg.image.load('image/head.png'), self.__head_size)

    def render(self, screen):
        x_screen, y_screen = Config.screen_size

        """display black jack head text"""
        screen.blit(self.__head_image, (x_screen/2-self.__head_size[0]/2, int(y_screen*0.05)))

        """display play button"""
        
