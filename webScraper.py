from deckutil import DeckUtil
from soupfunctions import get_soup
from deck import Deck
from fileutil import get_deck_paths
from apirequest import get_price_by_name
import sys

def should_get_from_web():
    return len(sys.argv) > 1 and sys.argv[1] == "web"

def get_ratios(cards):
    ratios = {}
    for card_name, count in cards.items():
        print(count, card_name)
        price = get_price_by_name(card_name)
        ratio = count/price
        ratio = "{:.2f}".format(ratio)
        ratios[card_name] = ratio
        print(card_name + " has a count:price ratio of " + str(ratio))

    return ratios

should_scrape_web = should_get_from_web()

if should_scrape_web:
    deck_paths = DeckUtil.get_decks_from_web()
    deck_paths = deck_paths[:1]
else:
    deck_paths = get_deck_paths()

card_dict = {}
for deck_path in deck_paths:
    deck_soup = get_soup(deck_path, True)
    deck = Deck(deck_soup)
    if should_scrape_web:
        deck.write_deck_to_file()
    
    print("Getting cards for: " + deck.get_title())
    for card in deck.get_cards():
        card_dict[card] = (card_dict.get(card, 0) + 1)

top_cards = DeckUtil.get_top_cards(card_dict, 2)

ratios = get_ratios(top_cards)