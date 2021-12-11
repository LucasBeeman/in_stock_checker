import requests
from bs4 import BeautifulSoup
from colorama import Fore
import time
from datetime import datetime
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.98 Safari/537.36'}

URL = "https://www.etokki.com/Omni-Sanwa-Edition"

while True:
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('li')[48]

    if results.text == "Availability: Out Of Stock":
        print(datetime.now())
        print(Fore.RED + "Item is out of stock :c\n\n")
    else:
        print(datetime.now())
        print(Fore.GREEN + "ITEM IS IN STOCK!!! :D\n\n")
    time.sleep(3600)
