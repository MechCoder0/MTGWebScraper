from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_soup_from_goldfish(sub_URL, is_dynamic):
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

def get_soup_from_file(file_path):
    with open(file_path) as f:
        return BeautifulSoup(f, 'html.parser')

def get_soup(sub_URL:str, is_dynamic:bool):
    if sub_URL.endswith(".html"):
        return get_soup_from_file(sub_URL)
    else:   
        return get_soup_from_goldfish(sub_URL, is_dynamic)