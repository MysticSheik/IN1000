#   *        (___)    *        (___)                (__)
#    \       (o o)     \       (o o)                (oo)
#     \-------\ /       \-------\ /          /-------\/        ________
#      |     ||O         |     ||O          / |     ||_|/    O _______
#      ||,---||          ||,---||          *  ||----|  --
#      ^^    ^^          ^^    ^^             ^^    ^
#                Twins                         Cow Catcher

# 2.1
fil = open("temperatur.txt")
temperaturer = []

for avakado in fil:
    temperaturer.append(int(avakado))

fil.close()

# 2.2
def gjennomsnitt(liste):
    total = 0
    for aspergers in liste:
        total += aspergers
    return total / len(liste)

print("Gjennomsnittstemperatur:", gjennomsnitt(temperaturer))
