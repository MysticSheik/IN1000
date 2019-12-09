class Celle:
    
    # Konstruktør
    def __init__(self):
        self._levende = False
    
    # Gjør en celle dead
    def sett_doed(self):
        self._levende = False
    
    # Gjør en celle levende
    def sett_levende(self):
        self._levende = True
    
    # Returnerer cellens status
    def er_levende(self):
        return self._levende
    
    # Returnerer tegnrepresentasjon av cellens status
    def hent_tegn(self):
        if self._levende:
            return "O"
        else:
            return "."
