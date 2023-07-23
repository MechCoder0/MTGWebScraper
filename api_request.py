import requests

base_url = "https://api.scryfall.com"

def get_price_by_name(name):
    tokenized_name = get_tokenized_name(name)
    request_url = base_url + "/cards/named?fuzzy=" + tokenized_name
    res = requests.get(request_url)
    card_info = res.json()
    price = float(card_info["prices"]["usd"])
    return price


def get_tokenized_name(name:str):
    return name.replace(" ", "+")