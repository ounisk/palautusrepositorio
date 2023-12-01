from sovelluslogiikka import Sovelluslogiikka
# Huom! ohje : mikään näistä EI palauta mitään!!!

class Summa:
    def __init__(self, sovelluslogiikka, syote):#, luku1): #, luku1):
        #super().__init__(io)
        #self.io = io
        #self.luku1 = luku1
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

    def suorita(self): #, arvo):
        #self.luku1 = int(self.io)
        #luku1 = int(self.io.read())
        #luku2 = int(self.io.read())
        #return arvo+ self.luku1 #+ self.luku2 #
        self._sovelluslogiikka.plus(self._syote())   ### tämä piti olla
        
class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        #super().__init__(io)
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

    def suorita(self):
        self._sovelluslogiikka.miinus(self._syote())
    

class Nollaus:   # ei saa syötettä
    def __init__(self, sovelluslogiikka, syote):
        #super().__init__(io)
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

    def suorita(self):
        #return 0
        #self._sovelluslogiikka.nollaa(self._syote())
        self._sovelluslogiikka.nollaa()