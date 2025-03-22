import pygame as pg
from config import Config
from game_card import Deck
from game_player import Player, Dealer

class GamePhase:
    DEAL = "DEAL"
    PLAYER = "PLAYER"
    DEALER = "DEALER"
    END = "END"

class GameUI:
    def __init__(self, screen):
        self.__screen = screen
        self.__phase = GamePhase.DEAL

    def init_game(self):
        self.__deck = Deck()
        self.__player = Player(self.__screen)
        self.__dealer = Dealer(self.__screen)

        for i in range(2):
            self.__dealer.deal_card(self.__deck)
            self.__player.deal_card(self.__deck)
        
        self.__phase = GamePhase.PLAYER

    def __player_turn(self, key):

        """give player make decition"""
        if key == pg.K_d: # player choose deal card
            self.__player.deal_card(self.__deck)
            if self.__player.is_bust:
                self.__phase = GamePhase.END
        elif key == pg.K_s: # player choose stand
            self.__phase = GamePhase.DEALER

    def __dealer_turn(self):
        pass

    def onKeyDown(self, key):
        if self.__phase == GamePhase.PLAYER:
            self.__player_turn(key)

    def render(self):
        """Fill background color"""
        self.__screen.fill(Config.BG_COLOR)
        self.__deck.render(self.__screen)


