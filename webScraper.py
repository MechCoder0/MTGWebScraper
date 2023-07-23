from deckutil import DeckUtil
from soupfunctions import get_soup
from deck import Deck
from fileutil import get_deck_paths
import sys

if len(sys.argv) > 1 and sys.argv == "web":
    deck_paths = DeckUtil.get_decks_from_web()
else:
    deck_paths = get_deck_paths()

card_dict = {}
for deck_path in deck_paths:
    deck_soup = get_soup(deck_path, True)
    deck = Deck(deck_soup)
    # deck.write_deck_to_file()
    
    print("Getting cards for: " + deck.get_title())
    for card in deck.get_cards():
        card_dict[card] = (card_dict.get(card, 0) + 1)

DeckUtil.get_top_cards(card_dict, 2)

