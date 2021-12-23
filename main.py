from getPrice import getPrice
from sourceUrl import MainPriceUrl
from getProfit import getProfit
from dotenv import load_dotenv
load_dotenv()
import os
from firebasestuff import firebasepost, firebaseget
from client.clientactions import changeActiveCoin, checkActiveCoin


def updateDB():
    rigurl = os.environ.get("myRigURL")
    #myRigURL

    profitarray = getProfit(rigurl)

    firebasepost(profitarray)



#Client / Miner Side
def checkCoin():
    best = firebaseget()
    
    bestCoin = best[0]
    currentCoin = checkActiveCoin()

    print("You are currently mining: "+ currentCoin +".")
    print("The most profitable coin rn is: "+ best[0] + " with a profit of: " + best[2]+" daily")

    if(bestCoin != currentCoin):
        print("You are not mining the most profitable Coin right now!")
        print("Changing active coin to: "+bestCoin)
        currentCoin = changeActiveCoin(bestCoin)
        print("You are now mining: "+ currentCoin)
    else:
        print("No need to change anything! :)")
        
    
