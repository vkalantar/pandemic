from board import City, Board
from player import Player
from cards import CardGroup

#blue
sf = City('San Francisco', 'blue', [])
chicago = City('Chicago', 'blue', [])
montreal = City('Montreal', 'blue', [])
ny = City('New York', 'blue', [])
atlanta = City('Atlanta', 'blue', [])
washington = City('Washington', 'blue', [])
london = City('London', 'blue', [])
madrid = City('Madrid', 'blue', [])
paris = City('Paris', 'blue', [])
essen = City('Essen', 'blue', [])
stp = City('St. Petersburg', 'blue', [])
milan = City('Milan', 'blue', [])


#yellow
la = City('Los Angeles', 'yellow', [])
mc = City('Mexico City', 'yellow', [])
miami = City('Miami', 'yellow', [])
bogota = City('Bogota', 'yellow', [])
lima = City('Lima', 'yellow', [])
santiago = City('Santiago', 'yellow', [])
ba = City('Buenos Aires', 'yellow', [])
saup = City('Sau Paulo', 'yellow', [])
lagos = City('Lagos', 'yellow', [])
khartoum = City('Khartoum', 'yellow', [])
kinshasa = City('Kinshasa', 'yellow', [])
johannesburg = City('Johannesburg', 'yellow', [])

#black
algiers = City('Algiers', 'black', [])
cairo = City('Cairo', 'black', [])
istanbul = City('Istanbul', 'black', [])
moscow = City('Moscow', 'black', [])
baghdad = City('Baghdad', 'black', [])
riyadh = City('Riyadh', 'black', [])
tehran = City('Tehran', 'black', [])
karachi = City('Karachi', 'black', [])
mumbai = City('Mumbai', 'black', [])
delhi = City('Delhi', 'black', [])
chennai = City('Chennai', 'black', [])
kolkata = City('Kolkata', 'black', [])

#red
beijing = City('Beijing', 'red', [])
seoul = City('Seoul', 'red', [])
shanghai = City('Shanghai', 'red', [])
osaka = City('Osaka', 'red', [])
hk = City('Hong Kong', 'red', [])
taipei = City('Taipei', 'red', [])
bangkok = City('Bangkok', 'red', [])
hcmc = City('Ho Chi Minh City', 'red', [])
manila = City('Manila', 'red', [])
jakarta = City('Jakarta', 'red', [])
sydney = City('Sydney', 'red', [])
tokyo = City('Tokyo', 'red', [])

#blue neighbors
sf.neighbors = [chicago, la, manila, tokyo]
chicago.neighbors = [sf, la, mc, atlanta, montreal]
montreal.neighbors = [chicago, washington, ny]
ny.neighbors = [montreal, washington, madrid, london]
atlanta.neighbors = [chicago, washington, miami]
washington.neighbors = [miami, atlanta, montreal, ny]
london.neighbors = [ny, madrid, paris, essen]
madrid.neighbors = [saup, ny, london, paris, algiers]
paris.neighbors = [madrid, london, essen, milan, algiers]
essen.neighbors = [london, paris, milan, stp]
stp.neighbors = [essen, istanbul, moscow]
milan.neighbors = [essen, paris, istanbul]

#yellow neighbors
la.neighbors = [sydney, sf, chicago, mc]
mc.neighbors = [la, chicago, miami, bogota, lima]
miami.neighbors = [mc, atlanta, washington, bogota]
bogota.neighbors = [mc, miami, lima, ba, saup]
lima.neighbors = [santiago, bogota, mc]
santiago.neighbors = [lima]
ba.neighbors = [bogota, saup]
saup.neighbors = [ba, bogota, madrid, lagos]
lagos.neighbors = [saup, khartoum, kinshasa]
khartoum.neighbors = [cairo, lagos, kinshasa, johannesburg]
kinshasa.neighbors = [lagos, khartoum, johannesburg]
johannesburg.neighbors = [kinshasa, khartoum]

#black neighbors
algiers.neighbors = [madrid, paris, istanbul, cairo]
cairo.neighbors = [algiers, istanbul, baghdad, riyadh, khartoum]
istanbul.neighbors = [algiers, milan, stp, moscow, baghdad, cairo]
moscow.neighbors = [istanbul, stp, tehran]
baghdad.neighbors = [istanbul, tehran, karachi, riyadh, cairo]
riyadh.neighbors = [cairo, baghdad, karachi]
tehran.neighbors = [delhi, karachi, baghdad, moscow]
karachi.neighbors = [baghdad, tehran, delhi, mumbai, riyadh]
mumbai.neighbors = [karachi, delhi, chennai]
delhi.neighbors = [kolkata, chennai, mumbai, karachi, tehran]
chennai.neighbors = [mumbai, delhi, kolkata, bangkok, jakarta]
kolkata.neighbors = [delhi, chennai, bangkok, hk]

#red neighbors
beijing.neighbors = [seoul, shanghai]
seoul.neighbors = [beijing, tokyo]
shanghai.neighbors = [beijing, seoul, tokyo, taipei, hk]
osaka.neighbors = [tokyo, taipei]
hk.neighbors = [kolkata, shanghai, taipei, manila, hcmc, bangkok]
taipei.neighbors = [hk, shanghai, osaka, manila]
bangkok.neighbors = [chennai, kolkata, hk, hcmc, jakarta]
hcmc.neighbors = [jakarta, bangkok, hk, manila]
manila.neighbors = [hcmc, hk, taipei, sf, sydney]
jakarta.neighbors = [chennai, bangkok, hcmc, sydney]
sydney.neighbors = [jakarta, manila, la]
tokyo.neighbors = [seoul, sf, osaka]

#add to list of all cities
allCities = [sf]
for cty in allCities:
    for n in cty.neighbors:
        if n not in allCities:
            allCities.append(n)

#create board and players
h1 = CardGroup([])
h2 = CardGroup([])
b = Board(allCities, [])
p1 = Player('Varqa', atlanta, h1, b)
p2 = Player('Nabil', johannesburg, h2, b)
b.addPlayer(p1)
b.addPlayer(p2)
import playerActions
import cards
a = cards.PlayerCard('city', madrid)
p1.hand.add(a)

                


