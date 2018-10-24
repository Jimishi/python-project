from quiz_jimmy_v2_Question import Question
from quiz_jimmy_v2_Question import Name
import sys

#   Add questions and possible answers here
question_display = [
    "What is my name? \n (a) Jimmy Ho \n (b) James Ho \n (c) Ho Wang Yu \n (d) Both a and c\n\n",
    "What is my age? \n (a) 20 \n (b) 21 \n (c) 22 \n (d) 23\n\n",
    "What is my home addres? \n (a) 37/632 St Kilda Road \n (b) 73/623 St Kilda Road \n (c) 67/362 Union Street \n (d) 63/632 St Kilda Road"
]

#   Add questions solutions here
questions = [
    Question(question_display[0], "d"),
    Question(question_display[1], "d"),
    Question(question_display[2], "a"),
]

def runQuiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(" You have scored " + str(score) + "/" + str(len(questions)))

runQuiz(questions)


