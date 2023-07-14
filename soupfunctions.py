from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_soup(sub_URL, is_dynamic):
    base_URL = "https://www.mtggoldfish.com"
    URL = base_URL + sub_URL
    print("Getting page for " + URL)
    if is_dynamic:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)
        driver.get(URL)
        content = driver.page_source
    else:
        page = requests.get(URL)
        content = page.content

    soup = BeautifulSoup(content, "html.parser")
    return soup

def get_decks():
    soup = get_soup("/deck/custom/commander#paper", False)
    elements = soup.find_all("span", class_="deck-price-paper")
    decks = []
    for el in elements:
        href = el.find("a").get("href")
        if bool(re.search(r'\d', href)):
            decks.append(href)
    return decks
