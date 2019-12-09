from random import randint
from celle import  Celle

class Spillebrett:
    
    # Konstruktør
    def __init__(self, bredde, hoyde):
        self._rader = bredde
        self._kolonner = hoyde
        self._rutenett = []
        
        # Fyll ting - maaagic
        for x in range(self._rader): # 10
            self._rutenett.append([])
            for y in range(self._kolonner): # 20
                self._rutenett[x].append(Celle())
        
        self._generasjonsnummer = 0
        self.generer()
    
    # Genererer en nullte generasjon som utgangspunkt
    def generer(self):
        for x in range(self._rader):
            for y in range(self._kolonner):
                rand = randint(0, 3)
                if rand == 3:
                    self._rutenett[x][y].sett_levende()
    
    # Finn Nabo
    def finn_nabo(self, x, y):
        naboliste = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                nabo_x = x + i
                nabo_y = y + j
                if (nabo_x == x and nabo_y == y) != True:
                    if (nabo_x < 0 or nabo_y < 0 or nabo_y > self._kolonner -1 or nabo_x > self._rader - 1) != True:
                        naboliste.append(self._rutenett[nabo_x][nabo_y])
        return naboliste
    
    # Oppdatering
    def oppdatering(self):
        dode_celler = []
        levende_celler = []
        
        for x in range(self._rader):
            for y in range(self._kolonner):
                naboer = self.finn_nabo(x, y)
                antall_levende = 0
                for celle in naboer:
                    if celle.er_levende():
                        antall_levende += 1
                
                # Levende Celle
                if self._rutenett[x][y].er_levende():
                    if antall_levende < 2 or antall_levende > 3:
                        levende_celler.append(self._rutenett[x][y])
                
                # Døende Celle
                if not self._rutenett[x][y].er_levende():
                    if antall_levende == 3:
                        dode_celler.append(self._rutenett[x][y])
                
        # Oppdater Celler
        for celle in dode_celler:
            celle.sett_levende()
        for celle in levende_celler:
            celle.sett_doed()
        self._generasjonsnummer += 1
    
    # Finn Antall Levende Celler
    def finn_antall_levende(self):
        antall_levende = 0
        for x in range(self._rader):
            for y in range(self._kolonner):
                if self._rutenett[x][y].er_levende():
                    antall_levende += 1
        return antall_levende
    
    # Tegn Brett
    def tegn_brett(self):
        # Tøm Terminalen
        for i in range(5):
            print()
        
        print("Generasjon", str(self._generasjonsnummer), ":")
        # Black Mag1c
        for y in range(self._kolonner):
            for x in range(self._rader):
                tegn = self._rutenett[x][y].hent_tegn()
                print(tegn, end = "")
            print()
