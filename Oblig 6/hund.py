class Hund:
    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10
    
    def spring(self):
        self.metthet -= 1
        if self.metthet < 5:
            self.vekt -= 1
    
    def spis(self, feithet):
        self.metthet += feithet
        if self.metthet > 7:
            self.vekt += 1
    
    def hentAlder(self):
        return self.alder
    
    def hentVekt(self):
        return self.vekt
