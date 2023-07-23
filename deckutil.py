from soupfunctions import get_soup
import re
import heapq

class DeckUtil:
    @staticmethod
    def get_decks_from_web():
        soup = get_soup("/deck/custom/commander#paper", False)
        elements = soup.find_all("span", class_="deck-price-paper")
        decks = []
        for el in elements:
            href = el.find("a").get("href")
            if bool(re.search(r'\d', href)):
                decks.append(href)
        return decks
    
    @staticmethod
    def get_top_cards(card_dict, number_of_cards):
        heap = []
        top_cards = {}
        for card_name, count in card_dict.items():
            heapq.heappush(heap, (-count, card_name))
                
        for x in range(number_of_cards):
            card = heapq.heappop(heap)
            print(card[1] + f" was seen {str(-card[0])} times")
            top_cards[card[1]] = -card[0]
        
        return top_cards
    