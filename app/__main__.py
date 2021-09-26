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
from parsing import cli_parsing
from classes import Game
from classes import CardDeck

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


def run():
    """ Summary:  this processes classes and functions from the app. """
    args = cli_parsing()
    game = Game()
    game.set_player_numbers(args.players)
    logging.info(game.get_player_number())

    card_deck = CardDeck()
    card_deck.create_deck()
    print(len(card_deck.deck))
    print(card_deck.get_card())
    # tens = ['jack', 'queen', 'king']
    # if any(i in card_deck.deck[2] for i in tens):
    #     print('True')
    # else:
    #     print('False')
    print(len(card_deck.deck))


if __name__ == '__main__':
    run()
