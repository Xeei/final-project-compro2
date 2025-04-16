import pygame as pg
from config import Config
from game_card import Deck
from game_player import Player, Dealer
from game_utils import GameUtils

class GamePhase:
    DEAL = "DEAL"
    PLAYER = "PLAYER"
    DEALER = "DEALER"
    END = "END"

class GameUI:
    def __init__(self, screen):
        self.__screen = screen
        self.__phase = GamePhase.DEAL
        self.__bg_image = GameUtils.load_image('image/bg_table2.jpg', Config.screen_size[1], Config.screen_size[0])

    def init_game(self):
        print("Game init")
        self.__screen.blit(self.__bg_image, (0,0))
        pg.display.flip()
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
        if key == pg.K_r:
            self.init_game()
        elif key == pg.K_q:
            pg.quit()
            exit()

    def __end_game_ui(self):
        print("Enter end phase")
        self.__player.show_card()
        self.__dealer.show_card(is_end_phase=True)

        p_score = self.__player.score
        d_score = self.__dealer.score

        overlay = pg.Surface(Config.screen_size, pg.SRCALPHA)
        overlay.fill((0, 0, 0, 179))
        self.__screen.blit(overlay, (0, 0))

        player_status = ""
        if self.__player.is_bust:
            player_status = "You Lost!"
        elif self.__dealer.is_bust or p_score > d_score:
            player_status = "You Win!"
        elif d_score > p_score:
            player_status = "You Lost!"
        else:
            player_status = "It's a Tie!"

        GameUtils.text_to_screen(self.__screen, player_status, Config.screen_size[0]//2, 200, color=(255,255,255), align="center", size=60)
        GameUtils.text_to_screen(self.__screen, 'Score: '+str(p_score), Config.screen_size[0]//2, 264, color=(255,255,255), align="center", size=60)

        GameUtils.text_to_screen(self.__screen, "Press `R` to play again", Config.screen_size[0]//2, 380, color=(255,255,255), align="center")
        GameUtils.text_to_screen(self.__screen, "`Q` for Quit game", Config.screen_size[0]//2, 480, color=(255,255,255), align="center")

    def renderKeyBind(self):
        pass

    def onKeyDown(self, key):
        if self.__phase == GamePhase.PLAYER:
            self.__player_turn(key)
        elif self.__phase == GamePhase.END:
            self.__end_game(key)

    def render(self):
        """Fill background color"""
        # self.__screen.fill(Config.BG_COLOR) 
        self.__deck.render(self.__screen)

        self.__dealer.render(x=526, y=59, is_dealer=True, is_end_phase=(self.__phase == GamePhase.END))

        self.__player.render(x=526, y=595)
        
        if self.__phase == GamePhase.DEALER:
            self.__dealer_turn()
        elif self.__phase == GamePhase.END:
            self.__end_game_ui()

        pg.display.flip()

