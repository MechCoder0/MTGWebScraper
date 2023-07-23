from file_util import write_to_file

class Deck:
    def __init__(self, soup):
        self.soup = soup
        self.set_title()
        self.set_cards()

    def set_title(self):
        title = self.soup.find("h1", class_="title").text
        title = title.replace("\n", "")
        title = title.replace(" ", "")
        self.title = title
    
    def set_cards(self):
        card_elements = self.soup.find_all("span", class_="card_id")
        card_set = set()
        for el in card_elements:
            a_tag = el.find("a")
            name = a_tag.text
            card_set.add(name)
        self.cards = card_set

    def write_deck_to_file(self):
        write_to_file(self.title + ".html", str(self.soup))

    def get_cards(self):
        return self.cards
    
    def get_title(self):
        return self.title