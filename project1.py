import time
import sys
import pickle
import os

#####   Help Menu   #####
def helpMenu():
    print("This is a QUIZ about Jimmy Ho \n")
    print("Press play to begin quiz \n")
    print("Get a score of 7 or higher to pass!")
    
def createProfile():
    name = input("Please Enter Your Name: \n") #In Python3.7 raw_input() was renamed to input()
    print('Type your name again for confirmation')

    nameresponse = input("> ")
    if(nameresponse == name):
        beginQuiz(name)
    else:
        print('You could not even type your name in twice, CYA')
        sys.exit()

#####   Shortening Questions in Quiz #####
def correct(score):
    print('............')
    score = score + 0
    print('You have ' +str(score) + ' points')

def incorrect(score):
    print('Correct!')
    score = score + 1 
    print('You have ' + str(score) + " point")

def askQuestion(questiontitle,question,one,two,three,four):
    print('### ' + questiontitle + ' ###')
    print(question)
    print('A. ' + one)
    print('B. ' + two)
    print('C. ' + three)
    print('D. ' + four)

#####   Quiz    #####
def beginQuiz(name):
    ## Introduction ##
    print(' \nOkay ' + name + ' You will be asked 10 questions about Jimmy Ho')
    print('Questions are multiple choice 4 choices each (A, B, C and D')

    score = 0
    score = int(score)  #turn score into and integer

    #####   Question 1  #####
    askQuestion("Question 1",
                "When was my Birthday?",
                "October 10th 1995",
                "October 16th 1994",
                "October 18th 1995" , 
                "October 19th 1996")
    quest1answer = "C"
    print('Your answer is...\n')
    quest1choice = input("> ")

    if(quest1choice != quest1answer):
        print('Come on man............')
        print('You are still on ' + str(score) + ' you ding dong')
    else:
        print("Good, atleast you got the easiest one")
        score = score + 1 
        print('You have ' + str(score) + ' point')

    #####   Question 2  #####
    askQuestion("Question 2",
                "What is my Chinese name is English spelling?",
                "He Hong Yu",
                "Ho Hong Yu",
                "He Wang Yu" , 
                "Ho Wang Yu")
    quest2answer = "D"
    print('Your answer is...\n')
    quest2choice = input("> ")

    if(quest2choice != quest2answer):
        correct(score)
    else:
        incorrect(score)
    
    #####   Question 3  #####
    askQuestion("Question 3",
                "What is the name of my High School?",
                "Scotch College",
                "Scotch High",
                "Wesley College" , 
                "Melbourne High")
    quest3answer = "A"
    print('Your answer is...\n')
    quest3choice = input("> ")

    if(quest3choice != quest3answer):
        correct(score)
    else:
        incorrect(score)

    #####   Question 4  #####
    askQuestion("Question 4",
                "What is my favorite type of computer game?",
                "FPS (First Person Shooters)",
                "RTS (Real Time Strategy)",
                "RPG (Role Playing Game" , 
                "Sports and Racing")
    quest4answer = "B"
    print('Your answer is...\n')
    quest4choice = input("> ")

    if(quest4choice != quest4answer):
        correct(score)
    else:
        incorrect(score)

    #####   Question 5  #####
    askQuestion("Question 5",
                "What is my favorite type of meat to eat?",
                "Beef",
                "Chicken",
                "Lamb" , 
                "Pork")
    quest5answer = "B"
    print('Your answer is...\n')
    quest5choice = input("> ")

    if(quest5choice != quest5answer):
        correct(score)
    else:
        incorrect(score)

    #####   Question 6  #####
    print('### Question 6 ###')
    print('What is the name of my Bachelor Degree course?')
    print('A. Bachelor of Computing Technology')
    print('B. Bachelor of Information Technology')
    print('C. Bachelor of Computer Science')
    print('D. Bachelor of Technology Computing Studies')

    quest6answer = "D"
    print('Your answer is...\n')
    quest6choice = input("> ")

    if(quest6choice != quest6answer):
        correct(score)
    else:
        incorrect(score)

    #####   Question 7  #####
    print('### Question 7 ###')
    print('What is my address?')
    print('A. 73/632 St Kilda Road')
    print('B. 36/637 St Kilda Road')
    print('C. 37/632 St Kilda Road')
    print('D. None of the above')

    quest7answer = "C"
    print('Your answer is...\n')
    quest7choice = input("> ")

    if(quest7choice != quest7answer):
        correct(score)
    else:
        incorrect(score)

    #####   Question 8  #####
    print('### Question 8 ###')
    print('What is the name of the Quirk of the main character in Hero Academia ?')
    print('A. One Punch')
    print('B. Full Cowl')
    print('C. Texas Smash')
    print('D. All for One')

    quest8answer = "D"
    print('Your answer is...\n')
    quest8choice = input("> ")

    if(quest8choice != quest8answer):
        correct(score)
    else:
        incorrect(score)

    #####   Question 9  #####
    print('### Question 9 ###')
    print('What do I like to call myself?')
    print('A. Poker God')
    print('B. King of Games')
    print('C. Fucking Talented')
    print('D. All of the above')

    quest9answer = "D"
    print('Your answer is...\n')
    quest9choice = input("> ")

    if(quest9choice != quest9answer):
        correct(score)
    else:
        incorrect(score)

    #####   Question 10 #####
    print('### Question 20 ###')
    print('What is the name of my only White friend?')
    print('A. William Hellier')
    print('B. Will Hellier')
    print('C. Adam William')
    print('D. Adam Will')

    quest10answer = "A"
    print('Your answer is...\n')
    quest10choice = input("> ")

    if(quest10choice != quest10answer):
        correct(score)
    else:
        incorrect(score)

    if (score >= 7):
        print('Good, you know enough about me')
    elif(score < 7):
        print('Not sure if I can even call you my friend')
        

#Title Screen
print('####################')
print('##     Welcome    ##')
print('##Do You Know Me? ##')
print('####################\n')

print('Please type in an available command, PLAY or HELP')

menu = input("> ")
if menu.lower() == ("play"):
    createProfile()
elif menu.lower() == ("help"):
    helpMenu()
while menu.lower() not in ["play", "help"]:
    print("Please enter PLAY or HELP")
    menu = input("> ")
    if menu.lower() == ("play"):
        createProfile()
    elif menu.lower() == ("help"):
        helpMenu()
        