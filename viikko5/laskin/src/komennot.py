from sovelluslogiikka import Sovelluslogiikka
# Huom! ohje : mikään näistä EI palauta mitään!!!

class Summa:
    def __init__(self, sovelluslogiikka, syote): #, vanha_tulos):
        #super().__init__(io)
        #self.io = io
        #self.luku1 = luku1
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self.vanha_tulos = 0
        #self._vanha_tulos = syote[1]

    def suorita(self): #, arvo):
        self.vanha_tulos = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.plus(self._syote())   ### tämä piti olla

    def kumoa(self): #, syote):
        self._sovelluslogiikka.aseta_arvo(self.vanha_tulos)

        
class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        #super().__init__(io)
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self.vanha_tulos = 0

    def suorita(self):
        self.vanha_tulos = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.miinus(self._syote())

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self.vanha_tulos)    
    

class Nollaus:   # ei saa syötettä
    def __init__(self, sovelluslogiikka, syote):
        #super().__init__(io)
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self.vanha_tulos = 0

    def suorita(self):
        #return 0
        #self._sovelluslogiikka.nollaa(self._syote())
        self.vanha_tulos = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self.vanha_tulos)     