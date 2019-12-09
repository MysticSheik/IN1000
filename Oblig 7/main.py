from spillbrett import Spillebrett

def hovedprogram():
    bredde = int(input("Skriv inn bredde på brettet: "))
    hoyde = int(input("Skriv inn høyde på brettet: "))
    brett = Spillebrett(bredde, hoyde)
    brett.tegn_brett() # Skriv ut Generasjon 0
    
    kommando = hent_kommando()
    while kommando != "q":
        if kommando == "":
            brett.oppdatering()
            brett.tegn_brett()
            print("Antall levende celler:", str(brett.finn_antall_levende()))
        kommando = hent_kommando()

def hent_kommando():
    print("Kommandoer:")
    print("- Trykk enter for å gå videre til neste generasjon")
    print("- q: Avslutter programmet")
    print()
    return input("Hva vil du gjøre? ")
    
hovedprogram()
