class Motorsykkel:
    def __init__(self, merke, reg_nr, km):
        self.merke = merke
        self.reg_nr = reg_nr
        self.km = km
    
    def kjor(self, km):
        self.km += km
    
    def hentKilometerstand(self):
        return self.km
    
    def skrivUt(self):
        print("Merke:", self.merke)
        print("Registreringsnummer:", self.reg_nr)
        print("Kilometerstand:", self.km)
