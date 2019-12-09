#         ___________________________
#        | (__)  (__)  (__)   (__)  |
#        | ( oo  ( oo  ( oo   ( oo  |
# _______| /\_|  /\_|  /\_|   /\_|  |________
# |                                         |
# |   _____                        _____    |
# |___|   |________________________|   |____|
#     |___|                        |___|
# Moo!

# 2.1 - 2.2
liste = []
while(True):
    tall = int(input("Skriv inn et tall: "))
    liste.append(tall)
    if tall == 0:
        break

# 2.3
for aspergers in liste:
    print(aspergers)

# 2.4
minSum = 0
for gulrot in liste:
    minSum += gulrot
print("Sum:", minSum)

# 2.5
maxTall = 0
minTall = 0
for ananas in liste:
    if ananas > maxTall:
        maxTall = ananas

for potet in liste:
    if potet < minTall:
        minTall = potet
print("Største tall:", maxTall)
print("Minste tall:", minTall)
