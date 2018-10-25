import random
import getpass
import sys
import time

def rollDice():
    diceface = [1, 2, 3, 4, 5, 6]
    roll = True
    while roll:
        userinput = getpass.getpass("Enter 1 to roll dice")
        if userinput == "1":
            print("Initializing ROLL DICE sequence")
            print("..."),
            time.sleep(1)
            print(random.choice(diceface))
        else:
            roll = False
            break
    
def flipCoin():
    flip = True
    coinface = ["Heads", "Tail"]
    while flip:
        userinput = getpass.getpass("Enter 2 to flip coin")
        if userinput == "2":
            print("Initializing FLIP COIN sequence")
            print(random.choice(coinface))
        else:
            flip = False
            break
    
    

print("###  WELCOME TO GAMBLING TOOLS   ###")
print("###  Enter 'roll' to roll a dice    ###")
print("###  Enter 'coin' to flip a coin    ###")

decision = input("")
if decision == "roll":
    rollDice()
if decision == "flip":
    flipCoin()

