import copy
import math
fact = math.factorial

#infection card
class InfCard:
    def __init__(self, city):
        self.city = city
        self.color = city.color
    def __repr__(self):
        return self.city.name + ' infection card'
    def __eq__(self, other):
        return self.city == other.city

#player card - can be a city, an event, or an epidemic
class PlayerCard:
    def __init__(self, typ, city = None, special = None):
        self.color = None
        self.typ = typ
        self.special = special
        self.city = city
        if typ == 'city':
            self.color = city.color
    def __repr__(self):
        if self.typ =='city':
            return self.city.name + ' city card'
        elif self.typ == 'event':
            return self.special + ' event card'
        elif self.typ == 'epidemic':
            return 'epidemic card'
    def __eq__(self, other):
        return self.city == other.city and self.special == other.special

    def __hash__(self):
        return hash(repr(self))

#collection of cards (currently can't be epidemics/other duplicate cards)
class CardGroup:
    def __init__(self, cards): #input is a list of cards
        self.cards = cards

    def __repr__(self):
        return 'A group of ' + str(len(self.cards)) + ' cards'

    def __eq__(self, other):
        return set(self.cards) == set(other.cards)

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i +=1
        if self.i < len(self.cards):
            return self.cards[self.i]
        else:
            raise StopIteration

    def add(self, crd): #add exceptions for duplicates?
        if isinstance(crd, list):
            self.cards.extend(crd)
        else:
            self.cards.append(crd)

    def remove(self, crd):
        if isinstance(crd, list):
            if set(crd) <= set(self.cards):
                for c in crd:
                    self.cards.remove(c)
            else:
                raise Exception('At least one card is not in the group')
        else:
            if crd in cards:
                self.cards.remove(crd)
            else:
                raise Exception('This card is not in the group')

    def num(self):
        return len(self.cards)

    def numType(self, t):
        n = 0
        for c in self.cards:
            if c.typ == t:
                n+=1

    def numColor(self, clr):
        n = 0
        for c in self.cards:
            if c.color == clr:
                n+=1


class InfDeck:
    def __init__(self, initial):
        self.stack = [initial]
        self.discard = []
    def __repr__(self):
        return 'A deck with ' + str(self.num) + ' cards and ' + str(len(self.stack)) + ' groups.'

    def num(self):
        n = 0
        for g in self.stack:
            n += g.num
        n += len(self.discard)
        return n

    def draw(self, card, i = -1):
        if card in self.stack[i]:
            self.stack[i].remove(card)
            self.discard.add(card)
            if self.stacks[i].num == 0:
                self.stacks[i].delete
        else:
            raise Exception('This card is not in the top stack.')

    def drawColor(self, color):
        #Given a color, this method will remove a card of that color (the first in the list)
        for c in self.stack[-1]:
            if c.color == color:
                self.draw(c)
                return c
            raise Exception('There is no card of this color in the top stack')

    def epidemic(self, card):
        #Given an InfCard, this method will run draw
        if card in stack[0]:
            self.draw(card,0)
            newStack = CardGroup(self.discard)
            self.discard = []
            stack.append(newStack)
        else:
            raise Exception('This card is not in the bottom of the deck')

    def colorProb(self, color, Tdraw, Cdraw):
        #Tdraw is the total number of cards drawn
        #Cdraw is the number of cards of the color
        #The function returns the probability of drawing that many cards of that color
        f = copy.deepcopy(self)
        n = f.stack[-1].num
        num = f.stack[-1].numColor(color) 
        if n <= Tdraw:
            Tdraw = Tdraw - n
            Cdraw = Cdraw - num
            f.stack.pop
            return colorProb(color, Tdraw, Cdraw)
        elif Cdraw > num or Cdraw>Tdraw:
            return 0
        else:
            return fact(num)/fact(num-Cdraw)*fact(n-num)/fact(n-num - (Tdraw-Cdraw))/(fact(n)/fact(n-Tdraw))
