# Oppgave:
# Lag et quiz-program som stiller spørsmål til brukeren, sjekker om de er
# riktige og teller poeng.

def still_sporsmaal(tekst):
    if type(tekst) == str:
        print("---------------------------")
        print(tekst)
        return input()
    else:
        print("Sporsmaalet er ikke en streng-variabel!")
        exit()

def print_svar(svar):
    print("Du svarte feil! (Det er nå du går i et hjørne og gråter litt c': )")
    print("Riktig svar var: " + svar)
    print("-------------------------------")

poeng = 0

print("Velkommen til det fantastiske quizprogrammet!")

if still_sporsmaal("Hvordan skrives 'God morgen' på japansk (roumaji)").lower() == "ohayou":
    poeng += 1
    print("Du svarte riktig, men dette var jo ikke så vanskelig?")
else:
    print_svar("ohayou")

if still_sporsmaal("Hvilken 19-åring ble brent på bålet for hekseri i 1431?").lower() == "jeanne d'arc":
    poeng += 1
    print("Du svarte riktig! Slightly stolt av deg c':")
else:
    print_svar("jeanne d'arc")

if still_sporsmaal("Hvilken spillfigure er kjent for å bruke sverdet 'parallell falchion'?").lower() == 'lucina':
    poeng += 1
    print("Du svarte riktig!")
else:
    print_svar("lucina")

if still_sporsmaal("Gitt at du er intern, hvor mye koster en dobbel latte i Escape?").lower() == '13':
    poeng += 1
    print("Du svarte riktig!")
else:
    print_svar('13')

if still_sporsmaal("Hvor mange er det i kø på kundeservice hos Telenor akkurat nå?").lower == "så mange at du legger på":
    poeng += 1
    print("Du svarte riktig!")
else:
    print_svar("så mange at du legger på")

if still_sporsmaal("Smaker ananas godt?").lower() == "nei! ananas er heresy så til de grader og kan brenne i helvete!":
    poeng += 1
    print("Ikke bare svarte du riktig, men du har også veldig god matsans!")
else:
    print_svar("nei! ananas er heresy så til de grader og kan brenne i helvete!")

print("-------------------------------")
print("Du fikk " + str(poeng) + " poeng!")
if poeng == 0:
    print("Dette var jo ikke så bra...")
elif poeng >= 4:
    print("Great!")
elif poeng >= 2:
    print("Du gjorde vel en fair jobb, I guess?")
