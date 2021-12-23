
def checkActiveCoin():

    return "Ethereum(ETH)"

def stopMining():
    #TODO: Stop mining the current coin by canceling the bat / program 
    return 1

def startMining(newCoin):
    #TODO: Start miming the newCoin by starting the bat / program 
    return 1 #s


def changeActiveCoin (newCoin):
    stopMining()
    startMining(newCoin) # TODO: add try/ catch
    return newCoin # return new coin if successful


