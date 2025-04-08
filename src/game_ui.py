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
        print("Game init")
        self.__deck = Deck()
        self.__player = Player(self.__screen)
        self.__dealer = Dealer(self.__screen)

        self.__deal_init_cards()

    def __deal_init_cards(self):
        for i in range(2):
            self.__dealer.deal_card(self.__deck)
            self.__player.deal_card(self.__deck)
        
        self.__phase = GamePhase.PLAYER   
        print("Enter player phase")
        self.__dealer.show_card()
        self.__player.show_card()

    def __player_turn(self, key):

        """give player make decition"""
        if key == pg.K_h: # player choose to hit (deal card)
            self.__player.deal_card(self.__deck)
            if self.__player.is_bust:
                self.__phase = GamePhase.END
        elif key == pg.K_s: # player choose stand
            self.__phase = GamePhase.DEALER

    def __dealer_turn(self):
        while self.__dealer.score < 17:
            self.__dealer.deal_card(self.__deck)
        self.__phase = GamePhase.END

    def __end_game(self, key):
        pass

    def __end_game_ui(self):
        print("Enter end phase")
        """Show all card"""
        self.__player.show_card()
        self.__dealer.show_card(is_end_phase=True)
        
        """Find who win"""
        p_score = self.__player.score
        d_score = self.__dealer.score

        if self.__player.is_bust:
            """player lost"""
            print("Player lose")
        elif self.__dealer.is_bust:
            """player win"""
            print("Player win")

        elif p_score > d_score:
            """player win"""
            print("Player win")

        elif d_score > p_score:
            """dealer win"""
            print("Dealer lose")

        else:
            print("tie")
            """tie"""


    def onKeyDown(self, key):
        if self.__phase == GamePhase.PLAYER:
            self.__player_turn(key)
        elif self.__phase == GamePhase.END:
            self.__end_game(key)

    def render(self):
        """Fill background color"""
        self.__screen.fill(Config.BG_COLOR)
        self.__deck.render(self.__screen)

        self.__dealer.render(x=300, y=50, is_dealer=True, is_end_phase=(self.__phase == GamePhase.END))

        self.__player.render(x=300, y=300)

        if self.__phase == GamePhase.DEALER:
            self.__dealer_turn()
        elif self.__phase == GamePhase.END:
            self.__end_game_ui()

        pg.display.flip()

