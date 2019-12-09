# Oppgavetekst: Les oppg. 5 i Oblig 6 PDF-en

class Person:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.hobbyer = []
    
    def legg_til_hobby(self, hobby):
        self.hobbyer.append(hobby)
        print("La til hobby:", hobby)
    
    def skriv_hobbyer(self):
        print("Hobbyer:")
        for hobby in self.hobbyer:
            print(hobby)
    
    def skriv_ut(self):
        print("Navn:", self.navn)
        print("Alder:", str(self.alder))
        self.skriv_hobbyer()

person = Person(input("Skriv inn et navn: "), int(input("Skriv inn en alder: ")))

kommando = ""
while kommando != "avslutt":
    kommando = input("Skriv inn en hobby (avslutt for å stenge programmet):")
    if kommando != "avslutt":
        person.legg_til_hobby(kommando)

print()
person.skriv_ut()
