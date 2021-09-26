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

import argparse
import logging
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


def cli_parsing():
    """ Parse the Command-line options """
    players_help = '(Optional) Using --players allows you to select how ' \
                   'many players will be in the game.' \
                   'Example:  --players=4, or --players 4.'
    parser = argparse.ArgumentParser(description='Initial Test of Parsing')
    parser.add_argument('--players', '--p', type=int, default=1, help=players_help)
    args = parser.parse_args()
    logging.info('%s - cli_parsing arguments:  %s', __name__, args)
    return args
