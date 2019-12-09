#          ^__^   /                \
#          (oo)  ( Milk is logical. )
#   /-------\/ --'\________________/
#  / |     ||
# *  ||W---||
#    ^^    ^^

# 1.1
def adder(tall1, tall2):
    return (tall1 + tall2)

print("Resultat 1:", adder(10, 10))
print("Resultat 2:", adder(25, 75))

# 1.2
# 1.3
tekst = input("Skriv inn noe tekst: ")
bokstav = input("Skriv inn en bokstav: ")

if len(bokstav) != 1:
    print("Du skrev ikke inn en bokstav :c")
    print("Shame on you!")
    exit()

def tellForekomst(minTekst, minBokstav):
    antallForekomster = 0
    for avakado in tekst:
        if avakado == bokstav:
            antallForekomster += 1
    return antallForekomster

print("Antall forekomster av:", bokstav)
print(tellForekomst(tekst, bokstav))

