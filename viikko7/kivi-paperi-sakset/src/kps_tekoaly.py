from tuomari import Tuomari
from tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset

class KPSTekoaly (KiviPaperiSakset):
    def __init__(self): #, tekoaly):
        self._tekoaly = Tekoaly()

    def toisen_siirto(self, ensimmäisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
    