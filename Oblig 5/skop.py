#                         (__)                        (__)
#                 ^^      (oo)                        (--)
#             ^^^^ /-------\/                        /-\/-\
#          ^^^^^  / |     ||                        /|    |\
#        ^^^^^   *  ||----||                       ^ |    | ^
#     ^^^^^^^^  ====^^====^^====                     |    |
# ^^^^^^^^^^^^^/                                     /----\
# ^^^^^^^^^^^^^^^^^^                                /    \ \
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^               ^      * ^
#      Cow Hanging Ten at Malibu           Cow sunning at Fort Lauderdale
#                                              (What a bod, huh guys?)

# Først definieres en funksjon, minFunksjon, som ikke tar noen parametere.
# Deretter defineres funksjonen hovedprogram, som ikke tar noen parametere.
# Til slutt kalles hovedprogram, og en variabel a med verdien 42 opprettes.
# Så opprettes en variabel b med verdi 0, som blir printet til terminalen. (0)
# Deretter endres verdien på b til a, slik at b nå er 42.
# Så settes a lik returverdien til minFunksjon(), og minFunksjon blir derfor
# kalt. 

# I minFunksjon opprettes først en midlertidig variabel x, som er en teller i
# en for loop som skal kjøres to ganger. I denne loopen opprettes en variabe
# c, med verdien 2. Denne blir printet, også økes verdien til c med 1, slik at
# c nå er lik 3. Så blir en variabel b opprettet som er lik 10, men denne 
# ligger i en annen minneadresse enn b fra hovedprogram.
# Deretter øker vi b med a, og her crasher programmet fordi det ikke finner
# en lokal variabel med navnet a i minFunksjon, fordi skop er en ting.

# Derfor returneres det bare en NameError til terminalen, og programmet
# kjører ikke videre.
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()
