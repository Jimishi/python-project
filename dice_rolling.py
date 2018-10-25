import random
import getpass
import sys

def rollDice():
    diceface = [1, 2, 3, 4, 5, 6]
    print(random.choice(diceface))

def flipCoin():
    coinface = ["Heads", "Tail"]
    print(random.choice(coinface))

print("###  WELCOME TO GAMBLING TOOLS   ###")
print("###  Enter '1' to roll a rice    ###")
print("###  Enter '2' to flip a coin    ###")


roll = True
while roll:
    userinput = getpass.getpass("Roll again by pressing 1")
    if userinput == "1":
        print("Initializing ROLL DICE sequence")
        rollDice()
    else:
        roll = False
        break
while True:
    if userinput == "2":
        print("Initializing FLIP COIN sequence")
        flipCoin()



