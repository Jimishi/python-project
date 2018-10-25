import random

class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self):
        print (("{} of {}").format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in [2,3,4, "Jack"]:
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw(self):
        return self.cards.pop()
    
    #def remove(self):
    #    del self.cards[0]
     #   del self.cards[0]
     #   del self.cards[0]
     #   del self.cards[0]

#class Player(object)
deck = Deck()
deck.shuffle()
#deck.remove()
deck.show()

#card = deck.draw()
#card.show()
