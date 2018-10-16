import time
import sys

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


#####   Quiz    #####
def beginQuiz(name):
    ## Introduction ##
    print(' \nOkay ' + name + ' You will be asked 10 questions about Jimmy Ho')
    print('Questions are multiple choice 4 choices each (A, B, C and D')

    score = 0
    score = int(score)  #turn score into and integer

    #####   Question 1  #####
    print('### Question 1 ###')
    print('When was my Birthday?')
    print('A. October 10th 1995')
    print('B. October 16th 1994')
    print('C. October 18th 1995')
    print('D. October 19th 1996')

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
    print('### Question 2 ###')
    print('What is my Chinese name is English spelling?')
    print('A. He Hong Yu')
    print('B. Ho Hong Yu')
    print('C. He Wang Yu')
    print('D. Ho Wang Yu')

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
    print('### Question 3 ###')
    print('What is the name of my High School?')
    print('A. Scotch College')
    print('B. Scotch High')
    print('C. Wesley College')
    print('D. Melbourne High')

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
    print('### Question 4 ###')
    print('What is my favorite type of computer game?')
    print('A. FPS (First Person Shooters)')
    print('B. RTS (Real Time Strategy)')
    print('C. RPG (Role Playing Game')
    print('D. Sports and Racing')

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
    print('### Question 5 ###')
    print('What is my favorite type of meat to eat?')
    print('A. Beef')
    print('B. Chicken')
    print('C. Lamb')
    print('D. Pork')

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
    print('### Question 6 ###')
    print('What is the name of my Bachelor Degree course?')
    print('A. Bachelor of Computing Technology')
    print('B. Bachelor of Information Technology')
    print('C. Bachelor of Computer Science')
    print('D. Bachelor of Technology Computing Studies')

    quest6answer = "D"
    print('Your answer is...\n')
    quest6choice = input("> ")

    if(quest6choice != quest2answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

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

    if(quest7choice != quest2answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

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

    if(quest8choice != quest2answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

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

    if(quest9choice != quest2answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

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

    if(quest10choice != quest2answer):
        print('............')
        score = score + 0
        print('You have ' +str(score) + ' points')
    else:
        print('Correct!')
        score = score + 1 
        print('You have ' + str(score) + " point")

    #results()


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