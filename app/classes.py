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
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


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

    def cards_total(self):
        """  cards_total method  """
        self.total = 52

    def cards_used(self):
        """  cards_used method  """
        self.used = 0
        self.total = self.total - self.used
