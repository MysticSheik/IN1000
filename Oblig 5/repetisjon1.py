#            o==+--
#            |  |\ \
#            |  | \ \    ____________________
#            |   \ \ \   |                  |
#            |    \ \ \  |  +------------+  |
#            |     \ \ \ |  |     (__)   |  |
#            |      \ \ \|  |     (oo)   |  |
#            |       \ \ |  | o\  .\/.   |  |
#            |        \ \|  | | \/    \  |  |
#          /---\       \ |  +------------+  |
#         /     \       \|                  |
#         |     |        |                  |
#         \     /        |                  |
#          \---/         |                  |
#                        |                  |
#                     --------------------------
#                    (                          )
#                     --------------------------
# 
#                   Cow-struction worker.

# 4.1
mineOrd = []

# 4.2
def slaaSammen(string_a, string_b):
    return string_a + string_b

# 4.3
def skrivUt(liste):
    for avakado in liste:
        print(avakado)

# 4.4
kommando = ""
while kommando != "s":
    kommando = input("Hva vil du gjøre? ")
    if kommando == "i":
        streng_a = input("Skriv inn tekst 1: ")
        streng_b = input("Skriv inn tekst 2: ")
        mineOrd.append(slaaSammen(streng_a, streng_b))
    elif kommando == "u":
        skrivUt(mineOrd)
