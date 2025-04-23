from game_card import Deck, Card
from config import Config
from game_utils import GameUtils
import pygame as pg
import os

class Event:
    def __init__(self, name, card, time_use, before_score, after_score):
        self.name: str = "" # deal | stand | f2c(first two card)
        self.card: Card = None
        self.time_use = 0 # compute from previous event
        self.before_score = 0
        self.after_score = 0

class Entity:
    def __init__(self, screen):
        self._cards: list[Card] = []
        self._screen = screen
        self._track_events: list[Event] = []

    def deal_card(self, deck:  Deck, is_init=False):
        # ev = Event()
        card = deck.deal()
        self._cards.append(card)
        # test = now
        if is_init:
            # self._track_events.append(Event())
            pass

    @property
    def score(self):
        possible_scores = [0]
        for card in self._cards:
            new_possible_scores = []
            card_scores = card.get_score()
            for score in possible_scores:
                for c_score in card_scores:
                    new_possible_scores.append(score + c_score)
            possible_scores = new_possible_scores

        valid_scores = [s for s in possible_scores if s <= 21]
        if valid_scores:
            return max(valid_scores)
        else:
            return min(possible_scores)
    
    @property
    def is_bust(self):
        if self.score > 21:
            return True
        return False
    
    def render(self, x, y, is_dealer=False, is_end_phase=False):
        for index, card in enumerate(self._cards):
            if is_dealer and index == 1 and not is_end_phase:
                back_card_path = os.path.join(Config.image_path, f"purple_back.png")
                hidden_card = GameUtils.load_card_image(back_card_path, 150)
                self._screen.blit(hidden_card, (x + index * 80, y))
            else:
                self._screen.blit(card.image, (x + index * 80, y)) 

class Dealer(Entity):
    def __init__(self, screen):
        super().__init__(screen)

    def show_card(self, is_end_phase=False):
        print("Dealer Card:")
        print("="*30)
        for _, card in enumerate(self._cards):
            if _ == 0 or is_end_phase:
                print(card)
            else:
                print("xx")
        print(self.score)
        print("="*30)

                
class Player(Entity):
    def __init__(self, screen):
        super().__init__(screen)

    def show_card(self):
        print("Player Card:")
        print("="*30)
        for _, card in enumerate(self._cards):
            print(card)
        print(self.score)
        print("="*30)
