import math
from cards import CardGroup, InfCard, PlayerCard, InfDeck

#A city is a location that can contain a player and disease cubes.
class City:
    def __init__(self, name, color, neighbors, cubes = {'black':0, 'red':0, 'yellow':0, 'blue':0, 'purple':0}, rs = 0):
        self.name = name
        self.color = color
        self.neighbors = neighbors
        self.cubes = cubes
        self.rs = rs
        
    def __repr__(self):
        return self.name
    
    def __eq__(self,other):
        return self.name==other.name

    def __hash__(self):
        return hash(repr(self))
    
    def changeCubes(self, color, n):
        cubes[color] +=n

    def outbreak(self, color, safe, n=0):
        n+=1
        for c in self.neighbors:
            if c.cubes[color]<3:
                c.cubes[color]+=1
            else:
                safe.add(c)
                n+= c.outbreak(color, safe, n)
                n+=1
                

#A board contains the information typically stored on the physical piece of cardboard, and updates to it.
class Board:
    def __init__ (self, cities, players):
        self.cities = cities
        self.players = players
        self.petriDish = {'black':24, 'red':24, 'yellow':24, 'blue':24}
        self.outbreaks = 0
        self.cured = {'black':False, 'red':False, 'yellow':False, 'blue':False}
        infCards = CardGroup([])
        pCards = CardGroup([])
        for cty in cities:
            infCards.add(InfCard(cty))
            pCards.add(PlayerCard('city', cty))
        self.infDeck = InfDeck(infCards)
        self.playerDeck = pCards #TODO: add epidemics and event cards
        self.playerDiscard = CardGroup([])
        self.researchStations = [];
        #continue adding to this class

    def addPlayer(self, p):
        self.players.append(p)
        
    def changePetriDish(self, color, n):
        self.petriDish[color] +=n

    def build(self, city):
        self.researchStations.add(city)

    def cure(self,color):
        self.cured[color] = 1

    def discard(self, card):
        self.playerDiscard.add(card)

    def infect(self, city, safe=([])):
        if city.cubes[city.color]<=3:
            city.changeCubes(color,1)
            changePetriDish(color, 1)
        else:
            outbreak(city)

    def epidemic(self, city):
        if city.cubes[city.color]>0:
            outbreak(city)
        city.cubes[city.color]=3

    def outbreak(self, city):
        n = city.outbreak(city.color, set([city]))
        self.outbreaks+=n
    
