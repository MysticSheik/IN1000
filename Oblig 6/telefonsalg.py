# 1.1
def innlesing(filnavn):
    ordok = {}
    fil = open(filnavn)
    for linje in fil:
        verdier = linje.split()
        assert len(verdier) == 2
        ordok[verdier[0]] = int(verdier[1])
    fil.close()
    return ordok

# 1.2
def maanedensSalgsperson(avakado):
    ananas = max(avakado, key = avakado.get)
    print("Månedens ansatte er", ananas, "med", str(avakado[ananas]), "salg.")

# 1.3
def totaltAntallSalg(sambandet):
    total = 0
    for value in sambandet.values():
        total += value
    return total

# 1.4
def gjennomSnittSalg(sambandet):
    return totaltAntallSalg(sambandet) / len(sambandet)

# 1.5
def hovedprogram():
    kattepus = innlesing("salgstall.txt")
    maanedensSalgsperson(kattepus)
    print("Aktive selgere denne måneden:", len(kattepus))
    print("Totalt antall salg:", totaltAntallSalg(kattepus))
    print("Gjennomsnittlig antall salg per person:", gjennomSnittSalg(kattepus))

# 1.6
hovedprogram()
