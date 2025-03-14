import pygame as pg
from config import Config
from game_ui import GameUI
class Button:

    def __init__(self, name: str, position):
        self.__name = name
        self.__position = position
        self.__font = pg.font.Font('font/Playfair_Display/PlayfairDisplay-VariableFont_wght.ttf', 40)
        self.__text = self.__font.render(self.__name, False, (0,0,0))
        self.__rect = self.__text.get_rect(center=self.__position)

    def is_in_bond(self, pos):
        return self.__rect.collidepoint(pos)

    def render(self, screen):
        screen.blit(self.__text, self.__rect)

        # pg.draw.rect(screen, "black", [self.__position[0], self.__position[1], self.__button_size[0], self.__button_size[1]])


class GameMenu:
    __x_screen, __y_screen = Config.screen_size
    __play_butt_position = (__x_screen//2, int(__y_screen*0.4))
    def __init__(self):
        self.__head_size = (600, 160)
        self.__head_image = pg.transform.smoothscale(pg.image.load('image/head.png'), self.__head_size)
        self.__play_butt = Button("PLAY", self.__play_butt_position)

    def onClick(self, pos):
        if self.__play_butt.is_in_bond(pos):
            return "PLAY"
    def render(self, screen):
        x_screen, y_screen = Config.screen_size

        """display black jack head text"""
        screen.blit(self.__head_image, (x_screen/2-self.__head_size[0]/2, int(y_screen*0.05)))

        """display play button"""
        self.__play_butt.render(screen)
        # play_butt_size = (300, 50)
        # pg.draw.rect(screen, "black", [x_screen/2-play_butt_size[0]/2, int(y_screen*0.4), play_butt_size[0], play_butt_size[1]])

