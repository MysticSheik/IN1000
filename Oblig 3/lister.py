# Oppgave 1.1
liste = [5, 8, 11]
print(liste[0])
print(liste[2])

# Oppgave 1.2
ny_liste = []
ny_liste.append(input("Skriv inn et navn: "))
ny_liste.append(input("Skriv inn et navn: "))
ny_liste.append(input("Skriv inn et navn: "))
ny_liste.append(input("Skriv inn et navn: "))

# Oppgave 1.3
if "Kathrine" in ny_liste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

# Oppgave 1.4
kombinert_liste = liste + ny_liste
for innhold in kombinert_liste:
    print(innhold)

kombinert_liste.pop()
kombinert_liste.pop()
for innhold in kombinert_liste:
    print(innhold)
