import pygame as pg
from config import Config
from game_card import Deck, Card
from game_player import Player, Dealer
from game_utils import GameUtils
from datetime import datetime
from game_db import GameDb
class GamePhase:
    DEAL = "DEAL"
    PLAYER = "PLAYER"
    DEALER = "DEALER"
    END = "END"

class Event:
    def __init__(self):
        self.name: str = "" # hit | stand | f2c(first two card)
        self.card: Card = None
        self.time = None
        self.before_score = 0
        self.after_score = 0

    def __str__(self):
        return f"Name: {self.name}, time: {self.time}, b: {self.before_score}, a: {self.after_score}"

class GameUI:
    def __init__(self, screen):
        self.__screen = screen
        self.__phase = GamePhase.DEAL
        self.__bg_image = GameUtils.load_image('image/bg_table2.jpg', Config.screen_size[1], Config.screen_size[0])
        self._start_time = None
        self._track_event: list[Event] = []
        self.__db = GameDb()
        self.__db_saved = False

    def init_game(self):
        print("=====Game init=====")
        self.__screen.blit(self.__bg_image, (0,0))
        pg.display.flip()
        self.__deck = Deck()
        self.__player = Player(self.__screen)
        self.__dealer = Dealer(self.__screen)
        self._start_time = datetime.now()
        self._end_time = None
        self._track_event = []
        self.__db_saved = False
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
        ev = Event()
        ev.before_score = self.__player.score
        ev.time = datetime.now()
        
        """give player make decition"""
        if key == pg.K_h: # player choose to hit (deal card)
            card = self.__player.deal_card(self.__deck)
            ev.name = "hit"
            ev.card = card
            if self.__player.is_bust:
                self.__phase = GamePhase.END
        elif key == pg.K_s: # player choose stand
            self.__phase = GamePhase.DEALER
            ev.name = "stand"
            

        if ev.name:
            ev.after_score = self.__player.score
            self._track_event.append(ev)

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
        # [print(ev) for ev in self._track_event]

        if not self.__db_saved:
            self._end_time = datetime.now()
            game_id = self.__db.insert_game(self._start_time, self._end_time, self.__player.score, self.__dealer.score)
            # print(game_id)
            self.__db.insert_game_events(game_id, self._track_event)
            for ev in self._track_event:
                print(ev)
            if game_id:
                self.__db_saved = True

    def renderKeyBind(self):
        "bg key bind"
        key_bind = pg.Rect(19, 572, 438, 210)
        pg.draw.rect(self.__screen, "#D9D9D9", key_bind, border_radius=10)

        "Hit key bind"
        GameUtils.text_to_screen(self.__screen, "H", 50, 627, color=(0,0,0), align="center", draw_border=True,border_color=(0,0,0), size=40)
        GameUtils.text_to_screen(self.__screen, "Hit (deal a card)", 220, 627, color=(0,0,0), align="center", size=40)
        
        "Stand key bind"
        GameUtils.text_to_screen(self.__screen, "S", 50, 725, color=(0,0,0), align="center", draw_border=True,border_color=(0,0,0), size=40)
        GameUtils.text_to_screen(self.__screen, "Stand (confirm card)", 260, 725, color=(0,0,0), align="center", size=40)

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
        self.renderKeyBind()
        if self.__phase == GamePhase.DEALER:
            self.__dealer_turn()
        elif self.__phase == GamePhase.END:
            self.__end_game_ui()


        pg.display.flip()

