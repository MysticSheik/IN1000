# Oppgave 4.1
def hent_alder():
    # Oppgave 4.2
    billettpris = 0
    
    alder = int(input("Skriv inn alderen din: "))
    
    # Oppgave 4.3
    if alder <= 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 50
    
    print("Du er " + str(alder) + " og billettprisen er " + str(billettpris) + ".")
# Problemet med prosedyren er hvis noen skriver inn noe som ikke er et tall,
# når de skriver inn alder. Et problem kunne vært om man stokket om litt på
# if-statementet, slik at noen som er over 17 år aldri vil kunne få pris på
# pensjonistbillett, selv om det er over 63 år. Eventuelt så kunne man også
# lagret billettype i en boolean eller string for å kunne skrive ut det i 
# tillegg, men det er ingen feil sånn egt, bare en forbedring elns.


for x in range(4):
    hent_alder()
