from game_card import Deck, Card
class Entity:
    def __init__(self, screen):
        self._cards: list[Card] = []
        self._screen = screen
    def deal_card(self, deck:  Deck):
        card = deck.deal()
        self._cards.append(card)

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

class Dealer(Entity):
    def __init__(self, screen):
        super().__init__(screen)

    def show_card(self):
        for _, card in enumerate(self._cards):
            if _ == 0:
                print(card)
            else:
                print("xx")
                
class Player(Entity):
    def __init__(self, screen):
        super().__init__(screen)

    def show_card(self):
        for _, card in enumerate(self._cards):
            print(card)
        print(self.score)

    def render(self):
        pass
