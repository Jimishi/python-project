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
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")
    
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
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

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
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

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
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

    #####   Question 6  #####
    askQuestion("Question 6",
                "What is the name of my Bachelor Degree course?",
                "Bachelor of Computing Technology",
                "Bachelor of Information Technology",
                "Bachelor of Computer Science" , 
                "Bachelor of Technology Computing Studies")
    quest6answer = "D"
    print('Your answer is...\n')
    quest6choice = input("> ")

    if(quest6choice != quest6answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

    #####   Question 7  #####
    askQuestion("Question 7",
                "What is my address?",
                "73/632 St Kilda Road",
                "36/637 St Kilda Road",
                "37/632 St Kilda Road" , 
                "None of the above")    
    quest7answer = "C"
    print('Your answer is...\n')
    quest7choice = input("> ")

    if(quest7choice != quest7answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

    #####   Question 8  #####
    askQuestion("Question 8",
                "What is the name of the Quirk of the main character in Hero Academia?",
                "One Punch",
                "Full Cowl" , 
                "Texas Smash",
                "All for One")
    quest8answer = "D"
    print('Your answer is...\n')
    quest8choice = input("> ")

    if(quest8choice != quest8answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

    #####   Question 9  #####
    askQuestion("Question 9",
                "What do I like to call myself?",
                "Poker God",
                "King of Games" , 
                "Fucking Talented",
                "All of the above")
    quest9answer = "D"
    print('Your answer is...\n')
    quest9choice = input("> ")

    if(quest9choice != quest9answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

    #####   Question 10 #####
    askQuestion("Question 10",
                "What is the full name of my only white friend?",
                "William Hellier",
                "Will Hellier" , 
                "Adam William",
                "Adam Will")
    quest10answer = "A"
    print('Your answer is...\n')
    quest10choice = input("> ")

    if(quest10choice != quest10answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

    if (score >= 7):
        print('Good, you know enough about me')
    elif(score < 7):
        print('Not sure if I can even call you my friend')
    elif(score == 10):
        print('You really know me very well!')
    
    text = 'The previous player, ' + name + 'got' + str(score) + 'in this QUIZ'

    saveFile = open('exampleFile.txt','w')
    saveFile.write(text)
    saveFile.close()

#Title Screen
def startGame():
    print('####################')
    print('##     Welcome    ##')
    print('##Do You Know Me? ##')
    print('####################\n')

    print('Please type in an available command, PLAY or HELP')

    menu = input(" ")
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

def saveScores(score):
    pickle_out = open("scores.pickle", "w")
    pickle.dump(score, pickle_out)
    pickle_out.close()

startGame()