import pygame as pg
from config import Config
from game_card import Deck
from game_player import Player, Dealer

class GameUI:
    def __init__(self, screen):
        self.__screen = screen

    def init_game(self):
        self.__deck = Deck()
        self.__player = Player()
        self.__dealer = Dealer()

        for i in range(2):
            self.__dealer.deal_card(self.__deck)
            self.__player.deal_card(self.__deck)

    def onKeyDown(self, key):
        if key == pg.K_s:
            self.__player.show_card()
        elif key == pg.K_d:
            self.__player.deal_card(self.__deck)

    def render(self):
        """Fill background color"""
        self.__screen.fill(Config.BG_COLOR)
        self.__deck.render(self.__screen)


