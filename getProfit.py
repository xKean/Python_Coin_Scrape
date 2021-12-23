# Import required modules
from lxml import html
import requests



def getProfit(url):
    # Request the page
    page = requests.get(url)

    # Parsing the page
    # (We need to use page.content rather than
    # page.text because html.fromstring implicitly
    # expects bytes as input.)
    tree = html.fromstring(page.content)

    i = 0
    xpathstatic = '//div[2]/table/tbody/tr'
    xpathstaticcoin= '/td[1]/div[2]/div[1]/a/text()'
    xpathstaticalgo = '/td[1]/div[2]/div[1]/text()'
    xpathstaticprofit = '/td[8]/strong/text()'
    iterator = str(i)

    profitarray = []

    while i < 15 :
        coin = ''
        algo = ''
        profit = ''

        i = i + 1
        iterator = str(i)
        coin = str(tree.xpath(xpathstatic+'['+iterator+']'+xpathstaticcoin))
        # Not interested in invalid shit and nicehash values
        if(coin != '[]'):
            algo = str(tree.xpath(xpathstatic+'['+iterator+']'+xpathstaticalgo))
            profit = str(tree.xpath(xpathstatic+'['+iterator+']'+xpathstaticprofit))
        # Slicing unnecassary stuff away
        coin = coin[2:-2]
        algo = algo[10:-4]
        profit = profit[4:-4]

        # Coin in coin, Algo in algo, Profit(24h) in profit

        profitstring = coin+";"+algo+";"+profit

        profitarray.append(profitstring)

    # Get out invalid values
    for entry in profitarray: 
        if(entry == ';;'):
            profitarray.remove(entry)
            continue
        print(entry)

    #Return Clean Profit array (Coinname, Algoname, Profit)
    return profitarray

        


