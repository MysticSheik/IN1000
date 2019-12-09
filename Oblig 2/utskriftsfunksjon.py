def print_personalia():
    navn = input("Skriv inn navn: ")
    bosted = input("Hvor kommer du fra: ")
    print("Hei, " + navn + "! Du er fra " + bosted)

for x in range(3):
    print_personalia()
