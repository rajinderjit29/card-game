from random import shuffle
class card:
    suits = ['spades', 'diamonds', 'clubs', 'hearts']
    values = [None, None, '2', '3', '4', '5', '6', '7' '8', '9', '10', 'Jack', 'King', 'Queen', 'Ace']
    def __init__(self, v, s):
        self.value = v
        self.suits = s
class Deck:
    def __init__ (self):
        self.cards = []
        for i in range (2, 15):
            for j in range (4):
                self.cards \
                    .append (card (i, j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards)==0:
            return 
        else :
            return self.cards.pop()
class player:
    def __init__ (self, name):
        self.wins = 0
        self.card = None
        self.name = name
class Game:
    def __init__(self):
        name1 = input("player 1 name")
        name2 = input("player 2 name")
        self.deck = Deck()
        self.p1 = player(name1)
        self.p2 = player(name2)
    def win(self, winner):
        w = '{} wins this round'
        w = w.format(winner)
        print(w)
    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} drew {} {} drew {}'
        d = d.format(p1n, p1c.value, p2n, p2c.value)
        print (d)
    def playgame(self):
        cards = self.deck.cards
        print('biginnig battle')
        while len(cards)>=2:
            m = "q to quit. Any key to play"
            response = input(m)
            if response == 'q':
                break
            else:
                p1n = self.p1.name
                p2n = self.p2.name
                p1c = self.deck.rm_card()
                p2c = self.deck.rm_card()
                self.draw(p1n, p1c, p2n, p2c)
                if p1c.value>p2c.value:
                    self.p1.wins+=1
                    self.win(self.p1.name)
                elif p2c.value>p1c.value:
                    self.p2.wins+=1
                    self.win(self.p2.name)
                else:
                    print("tie")
        win = self.winner(self.p1, self.p2)
        print("battle is over. {} win".format(win))
    def winner(self, p1, p2):
        if (p1.wins>p2.wins):
            return p1.name
        if (p2.wins>p1.wins):
            return p2.name
        return "its a tie"
game = Game()
game.playgame()