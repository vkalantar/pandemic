from player import Player
from copy import copy, deepcopy

    # Returns all the possible actions that the player could make
    # Actions are stored in a dictionary, with the function for
    # a given action as the keyword, and necessary info as the value
def possibleActions(p):
    #Note - needs to be fixed to reflect the new definition of PlayerHand
    #also possible to be imperative and not functional
    m = {}
    
    #walk
    m['walk'] = []
    for c in p.l.neighbors:
        m['walk'].append(c)
        
    #directFlight, charterFlight, buildRS
    m['charterFlight'] = []
    m['directFlight'] = []
    m['buildRS'] = []
    for c in p.hand:
        m['charterFlight'].append(c)
        if c.city == p.l:
            m['directFlight'] = [c]
            if p.l.rs == 0: 
                m['buildRS'] = [c]
                    
    #researchFlight
    m['researchFlight'] = []            
    if p.l.rs != 0:
        for cty in p.board.researchStations:
            if cty != p.l:
                m['researchFlight'].append(c)
        
    #treat
    for color, n in p.l.cubes.items():
        if n>=1:
            m['treat'].append(color)
            
    #giveCard, takeCard
    m['giveCard'] = []
    m['takeCard'] = []
    for p2 in p.board.players:
        if p2 != p:
            for c in p.hand:
                m['giveCard'].append((p2, c))
            for c in p2.hand:
                m['takeCard'].append((p2,c))

    #cureDisease - unfinished

    return m

#Gives a set of all possible cities that a player can move to
#with a single action, in the form of tuples of the city and the cost in cards.
#If a city can be reached in multiple ways, all will be returned.
#However, if one option is strictly better, only it will be returned.
def singleMovement(p):
    newCities = {}
    actions = possibleActions(p)
    for w in actions['walk']:
        newCities[w] = [[]]
    for rf in actions['researchFlight']:
        newCities[rf] = [[]]
    for cf in actions['charterFlight']:
        if cf.city not in newCities:
            newCities[cf.city] = [[cf]]
    for df in actions['directFlight']:
        for cty in p.board.cities:
            if cty not in newCities:
                newCities[cty] = [[df]]
            elif newCities[cty] != [[]]:
                newCities[cty].append([df])        
    return newCities

#Returns a dictionary of all possible cities that a player can reach in exactly n moves, and their costs.
#If a city can be reached in multiple ways, all will be returned.
#However, if one option is strictly better, only it will be returned.
                
def manyMovements(p, n):
    if n==1: #base case
        return singleMovement(p)
    else: #recursive step
        newCities = {}
        prev = manyMovements(p,n-1)
        for prev_cty, prev_costs in prev.items(): #consider each city
            for pc in prev_costs: #consider each cost to reach each city
                temp_player = Player(p.name, prev_cty, deepcopy(p.hand), p.board)
                temp_player.hand.remove(pc)
                newStep = singleMovement(temp_player)
                for cty, cost in newStep.items():
                    for c in cost: #look at each possible cost
                        newCost = pc + c
                        if cty in newCities: #reaching an old city
                            status = 'good'
                            #recheck for better options
                            for q in newCities[cty]:
                                if set(q) <= set(newCost):
                                    status = 'worse'
                                elif set(q) >= set(newCost):
                                    newCities[cty].remove(q)
                            if status == 'good':
                                newCities[cty].append(newCost)
                        else: #reaching a new city
                            newCities[cty] = [newCost]
        return newCities

#returns a dict of ways to reach a city, with the key being the number of steps
#The method stops when the city can be reached with no card expenditure
def reachCity(p, c):
    done = false
    whie not done:
        

#Returns a dictionary of all cities that can be treated
#along with the number of each cube color removed, and the cost in cards
#def manyTreatments(p, n):
        
    
    
    
        
    
    
