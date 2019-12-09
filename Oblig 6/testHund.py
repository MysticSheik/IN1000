from hund import Hund

def hovedprogram():
    hund = Hund(9, 6)
    for x in range(2):
        print("Vekt:", hund.hentVekt())
        hund.spring()
    for x in range(2):
        print("Vekt:", hund.hentVekt())
        hund.spis(2)

hovedprogram()
