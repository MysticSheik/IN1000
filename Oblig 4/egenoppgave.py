#                                   @
#                (__)    (__) _____/
#             /| (oo) _  (oo)/----/_____    *
#   _o\______/_|\_\/_/_|__\/|____|//////== *- *  * -
#  /_________   \   00 |   00 |       /== -* * -
# [_____/^^\_____\_____|_____/^^\_____]     *- * -
#       \__/                 \__/

# Et​ ​ forslag​ ​ er​ ​ å programmere​ ​ et​ ​ system​ ​ som​ ​ lar​ ​ bruker​ ​ holde​ ​ styr​ ​ på,​ ​ legge​ ​ til​ ​ og​ ​ skrive​ ​ ut​ ​ venners bursdager

bursdager = {}

def legg_til_bursdag(navn, bursdag):
    bursdager[navn] = bursdag
    print("La til bursdag:", str(bursdag), "hos", navn)

def print_bursdag(navn):
    if not navn in bursdager:
        print("Fant ingen bursdag, gråte gråte")
        return
    print(navn, "har bursdag:", str(bursdager[navn]))

def print_bursdager():
    for key, value in bursdager.items():
        print(key,"har bursdag",value)

def hent_kommando():
    print("Velkommen til bursdagssystemet mitt")
    print("legg til: Legger til eller endrer en bursdag")
    print("vis: Skriver ut en bursdag")
    print("vis alle: Skriver ut alle bursager")
    print("avslutt: Går ut av programmet")
    print()
    return input("Hva vil du gjøre? ")

while(True):
    kommando = hent_kommando()    
    
    # Legg til
    if kommando == "legg til":
        navn = input("Hvem sin bursdag vil du endre eller legge til? ")
        bursdag = input("Skriv inn bursdag: ")
        legg_til_bursdag(navn, bursdag)
    
    # Vis
    elif kommando == "vis":
        navn = input("Hvem sin bursdag vil du se? ")
        print_bursdag(navn)
    
    # Vis Alle
    elif kommando == "vis alle":
        print_bursdager()

    # Avslutt
    elif kommando == "avslutt":
        break
    
    print()
