class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Name:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_input(cls):
        return cls(
            input('Name: ')
        )

player = Name.from_input()
print(player.name)

