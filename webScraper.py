from soupfunctions import get_decks, get_soup

def map_cards(deck_uri):
    soup = get_soup(deck_uri, True)
    card_elements = soup.find_all("span", class_="card_id")
    card_set = set()
    for el in card_elements:
        a_tag = el.find("a")
        name = a_tag.text
        card_set.add(name)
    return card_set

decks = get_decks()
decks = decks[:2]
card_dict = {}

for deck in decks:
    cards = map_cards(deck)
    for card in cards:
        card_dict[card] = (card_dict.get(card, 0) + 1)

for card_name, count in card_dict.items():
    if(count > 1):
        print(card_name + f" was seen {count} times")