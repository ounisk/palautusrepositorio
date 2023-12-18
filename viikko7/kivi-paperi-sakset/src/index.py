from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from pelitehdas import Pelitehdas


def main():

    pelit = {"a": Pelitehdas.luo_kaksinpeli(),
             "b": Pelitehdas.luo_yksinpeli(),
             "c": Pelitehdas.luo_vaikea_yksinpeli()
             }

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        #if vastaus.endswith("a"):
        #    print(
        #        "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        #    )

        #    kaksinpeli = KPSPelaajaVsPelaaja()
        #    kaksinpeli.pelaa()
        #elif vastaus.endswith("b"):
        #    print(
        #        "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        #    )

        #    yksinpeli = KPSTekoaly()
        #    yksinpeli.pelaa()
        #elif vastaus.endswith("c"):
        #    print(
        #        "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        #    )

        #    haastava_yksinpeli = KPSParempiTekoaly()
        #    haastava_yksinpeli.pelaa()
        if vastaus in pelit:
            pelit[vastaus].pelaa()
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        else:
            break


if __name__ == "__main__":
    main()
