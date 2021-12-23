# Import libraries
import requests
from lxml import html
from bs4 import BeautifulSoup

def getPrice(coinmarketurl):

    # Set the URL you want to webscrape from
    url = coinmarketurl

    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    myprice = soup.find_all("div", {"class": "priceValue"})

    pricestring = myprice[0].text
    print(pricestring)

    return pricestring














