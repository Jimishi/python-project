class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Name:
    def __init__(self):
        self.name = "Enter your name: " 

    def ask(self):
        while 1:
            name = input("Name: ")
            if name == "":
                print("Retry")
            else:
                print("Hello ", name)
                break
        
        self.name = name

