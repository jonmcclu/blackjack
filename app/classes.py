"""
Blackjack
Copyright (C) 2021  Jonas McClure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging
import random
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


class Game:
    """  Game Class  """
    def __init__(self):
        self.player_numbers = 0
        self.rounds_max = 0
        self.rounds = 0

    def set_player_numbers(self, player_number):
        """  set_player method  """
        self.player_numbers = player_number

    def get_player_number(self):
        """  get_player method  """
        return self.player_numbers

    def set_rounds(self, round_count):
        """  get_rounds method  """
        self.rounds_max = round_count

    def add_round(self):
        """  add_round method  """
        self.rounds += 1


class Player:
    """  Player Class  """
    def __init__(self):
        self.name = ''
        self.cards = []
        self.score_round = 0
        self.score_overall = 0

    def player_name(self):
        """  player_name method  """
        self.name = 'Get input from user'

    def player_score(self):
        """  player_score method  """
        self.score_round = 0
        self.score_overall = 0


class CardDeck:
    """  CardDeck Class  """
    def __init__(self):
        self.total = 52
        self.used = 0
        self.deck = []

    def cards_total(self):
        """  cards_total method  """
        self.total = 52

    def cards_used(self):
        """  cards_used method  """
        self.used = 0
        self.total = self.total - self.used

    def create_deck(self):
        """  create_deck method  """
        suites = ['clubs', 'diamonds', 'hearts', 'spades']
        faces = ['ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        self.deck = [[f + ' of ' + s, f] for s in suites for f in faces]
        return self.deck

    def get_card(self):
        """  get_card """
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
