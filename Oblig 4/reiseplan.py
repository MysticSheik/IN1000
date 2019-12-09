#          (__)               (__)  |    |  (__)
#          (--)               (--)  |    |  (--)
#   /-------\/   /o    /-------\/   |    I   \/-------\
#  / |  M  |----< o   / |  L  |----<T    I>----|  D  | \
# *  ||----|   /  o  *  ||----|     I    I     |----||  *
#    ^^    ^      |     ^^    ^          |     ^    ^^
#                 |                      |
#               Teenage Mutant Ninja Cows

# 4.1
steder = []
for x in range(0, 5):
    steder.append(input("Skriv inn et reisemål: "))

# 4.2
klesplagg = []
avreisedatoer = []

for x in range(0, 5):
    klesplagg.append(input("Skriv inn et klesplagg: "))
    avreisedatoer.append(input("Skriv inn en avreisedato: "))

# 4.3
reiseplan = [steder, klesplagg, avreisedatoer]

# 4.4
for liste in reiseplan:
    print(liste)

# 4.5
i1 = int(input("Skriv inn index 1: "))
if (i1 < 0) and (i1 >= len(reiseplan)):
    print("Ugydig input! Din gjøk!")
    exit()

i2 = int(input("Skriv inn index 2: "))
if (i2 < 0) or (i2 >= len(reiseplan[i1])):
   print("Ugyldig input! Din gjøk!")
   exit()

print("Reiseplan-ting:", reiseplan[i1][i2])
