from soupfunctions import get_soup
import re

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