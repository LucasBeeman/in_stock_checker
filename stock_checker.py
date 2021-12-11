import requests
from bs4 import BeautifulSoup
from colorama import Fore
import time
from datetime import datetime

#bypases security by pretending that the scraper is using a "user agent" tag
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.98 Safari/537.36'}

URL = "https://www.etokki.com/Omni-Sanwa-Edition"

#loops checking a website every hour
while True:
    #gets the HTML of the webadress of the URL, and bypasses security with "headers=headers"
    page = requests.get(URL, headers=headers)
    #gets all of the HTML
    soup = BeautifulSoup(page.content, 'html.parser')\
    #finds a specific part of the html that I need. It tells me if the item is out of stock
    results = soup.find_all('li')[48]
    
    #if the item is out of stock, say that it's out of stock
    if results.text == "Availability: Out Of Stock":
        print(datetime.now())
        print(Fore.RED + "Item is out of stock :c\n\n")
    #if item is out of stock, say that it's in stock
    else:
        print(datetime.now())
        print(Fore.GREEN + "ITEM IS IN STOCK!!! :D\n\n")
    #wait for an hout
    time.sleep(3600)
