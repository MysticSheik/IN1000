from motorsykkel import Motorsykkel

def hovedprogram():
    motorsykler = []
    motorsykler.append(Motorsykkel("BSA", "AX0524", 465))
    motorsykler.append(Motorsykkel("Yamaha", "BZ626", 9000))
    motorsykler.append(Motorsykkel("Indian", "LT5291", 64025))
    for motorsykkel in motorsykler:
        motorsykkel.skrivUt()
    motorsykler[2].kjor(60)
    print(motorsykler[2].hentKilometerstand())

hovedprogram()
