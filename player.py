class Player:
    def __init__(self, name, location, hand, board):
        self.name = name
        self.l = location
        self.hand = hand
        self.board = board

    def __repr__(self):
        return self.name + ' Player'

    def __eq__(self, other):
        return self.name == other

        
    def walk(self, city):
        if city in self.l.neighbors:
            self.l = city
        else:
            raise Exception('This is not a neighboring city.')

    def directFlight(self, card):
        if card in self.hand:
            self.l = card.city
            self.discard(card)
        else:
            raise Exception('You do not have a card for this city')

    def charterFlight(self, card, city):
        if card in self.hand and self.l == card.city:
            self.l = city
            self.discard(card)
        else:
            raise Exception('You either do not own this card, or are not in this city')
        
    def researchFlight(self, city):
        if self.l.rs == 1 and city.rs == 1:
            self.l = city
        else:
            raise Exception('One of these cities is missing a research station')

    def treat(self,color):
        if self.l.cubes[color]>0:
            self.l.changeCubes(color, -1)
            self.board.addToPetriDish(color,1)
        else:
            raise Exception('There are no cubes of this color')

    def giveCard(self, card, other):
        if self.l == other.l and self !=other and card in self.hand:
            #fix this later
            self.hand.remove(card)
            other.hand.add(card)
        else:
            raise Exception('Either you don\'t have this card, or are not in the same city')

    def takeCard(self, card, other):
        if self.l == other.l and self !=other and card in other.hand:
            #fix this later
            self.hand.add(card)
            other.hand.remove(card)
        else:
            raise Exception('Either they don\'t have this card, or are not in the same city')

    def cureDisease(self, color, cards):
        for c in cards:
            if c.color != color or c not in self.hand:
                raise Exception('You do not have the necesary cards')
        if self.l.rs == 1:
            for c in cards:
                self.hand.remove(c)
            self.board.cure(color)
        else:
            raise Exception ('There is no research station here')

    def buildRS(self, card):
        if self.l == card.city and card.city.rs==0 and card in self.hand:
            card.city.rs =1
            self.board.build(card.city)
            self.discard(card)
        else:
            raise Exception ('You either are not in the right city, don\'t have the right card, or there is a research station already')
        
    def discard(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.board.discard(card)
        else:
            raise Exception ('This card is not in your hand')

            
            
