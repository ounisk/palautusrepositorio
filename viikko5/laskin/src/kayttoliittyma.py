from komennot import Summa, Erotus, Nollaus
from enum import Enum
from tkinter import ttk, constants, StringVar

#from sovelluslogiikka import Sovelluslogiikka 


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._edellinen_komento_olio = ""

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote), # , self._lue_vanha_arvo),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            #Komento.KUMOA: Summa(sovelluslogiikka, self._lue_syote, self._lue_vanha_arvo) # ei ehkä tarvita täällä...
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):  # tuleeko try except tänne, onko edes tarpeen?
    
        try:
            #vanha_arvo = int(self._arvo_var.get())
            return int(self._syote_kentta.get()) #, int(self._arvo_var.get())) 
        except ValueError:  
            pass

    def _suorita_komento(self, komento):
       
        if komento == Komento.KUMOA:   #eli toiminnon kumoamiseen
            self._edellinen_komento_olio.kumoa()

        else:
            komento_olio = self._komennot[komento]
            #komento_olio.suorita()
            self._edellinen_komento_olio = komento_olio #laittaa muistiin mikä oli suoritettu toiminto

            komento_olio.suorita()    

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:   
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())    # muutettu tulos_var.set -> _arvo_var ja sovlog.tulos --> aov.log.arvo()
        #edellinen_komento_olio = self._komennot[komento]    # Eli laittaa muistiin mikä oli suoritettu toiminto
        #print("vanha_komento")
        #print(self._edellinen_komento_olio)


    #def _suorita_komento(self, komento):    # Vanha, joka pitää refaktoroida!
    #    arvo = 0
    #    try:
    #        arvo = int(self._syote_kentta.get())
    #    except Exception:
    #        pass

    #    if komento == Komento.SUMMA:
    #        self._sovelluslogiikka.plus(arvo)
    #    elif komento == Komento.EROTUS:
    #        self._sovelluslogiikka.miinus(arvo)
    #    elif komento == Komento.NOLLAUS:
    #        self._sovelluslogiikka.nollaa()
    #    elif komento == Komento.KUMOA:
    #        pass

    #    self._kumoa_painike["state"] = constants.NORMAL
   # 
    #    if self._sovelluslogiikka.arvo() == 0:
    #        self._nollaus_painike["state"] = constants.DISABLED
    #    else:
    #        self._nollaus_painike["state"] = constants.NORMAL
#
#        self._syote_kentta.delete(0, constants.END)
#        self._arvo_var.set(self._sovelluslogiikka.arvo())
