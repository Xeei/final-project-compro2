import random
import pygame as pg
from config import Config
import os
from game_utils import GameUtils


class Card:
    def __init__(self, symbol: str, number: str):
        self.__symbol = symbol
        self.__number = number
        image_path = os.path.join(
            Config.image_path, f"{self.__number+self.__symbol}.png"
        )
        self.__image = GameUtils.load_card_image(image_path, 150)

    @property
    def image(self):
        return self.__image

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def get_score(self):
        if self.__number in ["J", "Q", "K"]:
            return [10]
        elif self.__number == "A":
            return [1, 11]
        else:
            return [int(self.__number)]

    def show_card(self, screen, position):
        screen.blit(self.__image, (100, 200))

    def __str__(self):
        return f"{self.__symbol}:{self.__number} -> {','.join(str(score) for score in self.get_score())}"


class Deck:
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    symbols = ["S", "H", "D", "C"]
    __deck_path = os.path.join(Config.image_path, "purple_back.png")
    __deck_hieght = 150

    def __init__(self):
        self.__deck = [
            Card(symbol, number) for number in self.numbers for symbol in self.symbols
        ]
        self.__back_deck = GameUtils.load_card_image(
            self.__deck_path, self.__deck_hieght
        )
        self.suffle()

    @property
    def remain(self):
        return len(self.__deck)

    def suffle(self):
        random.shuffle(self.__deck)

    def display_all_card(self, screen):
        for c in self.__deck:
            c.show_card(screen)

    def render(self, screen):
        x, y = (
            int(Config.screen_size[0] * 0.85),
            int(Config.screen_size[1] * 0.5 - self.__deck_hieght / 2),
        )
        screen.blit(self.__back_deck, (x, y))
        self.text_to_screen(
            screen, f"Remain Cards: {len(self.__deck)}", x, y + self.__deck_hieght, 20
        )

    @staticmethod
    def text_to_screen(
        screen,
        text,
        x,
        y,
        size=50,
        color=(200, 000, 000),
        font_type="font/Playfair_Display/PlayfairDisplay-VariableFont_wght.ttf",
    ):
        try:

            text = str(text)
            font = pg.font.Font(font_type, size)
            text = font.render(text, True, color)
            screen.blit(text, (x, y))

        except Exception as e:
            raise e

    def deal(self):
        card = self.__deck.pop()
        return card
