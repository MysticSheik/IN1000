#          (__)
#          (oo)                       U
#   /-------\/                    /---V
#  / |     ||                    * |--|                       .
# *  ||----||
#    ^^    ^^
#
# Cow at 1 meter.         Cow at 100 meters.        Cow at 10,000 meters.
 
# 1.1
def addisjon(a, b):
    return a + b

print(addisjon(10, 20))

# 1.2
def subtraksjon(a, b):
    return a - b

assert subtraksjon(20, 10) == 10
assert subtraksjon(5, 2) == 3
assert subtraksjon(25, 5) == 20

def divisjon(a, b):
    return a / b

assert divisjon(10, 5) == 2
assert divisjon(9, 3) == 3
assert divisjon(20, 10) == 2

# 1.3
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

print(4, "cm = ", tommerTilCm(4), "tommer")
assert tommerTilCm(10) == 10 * 2.54

# 1.4
def skrivBeregninger():
    x = float(input("Skriv inn et tall: "))
    y = float(input("Skriv inn et tall til: "))
    print(x, "+", y, "=", addisjon(x, y))
    print(x, "-", y, "=", subtraksjon(x, y))
    print(x, "/", y, "=", divisjon(x, y))
    
    tommer = float(input("Skriv inn antall tommer: "))
    print(tommer, "tommer =", tommerTilCm(tommer), "tommer")

# 1.5
skrivBeregninger()
