#najprej konstante
import random
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '0'
NAPACNA_CRKA = '-'

ZACETEK = 'Z'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() #pravilno geslo
        self.crke = crke.upper() # do sedaj ugibane crke
        #vse stvari v igri so samo velike črke

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    
    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        return all([i in self.crke for i in self.geslo])
        #['a' in self.crke(), 'x' in self.crke()...]

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    
    def pravilni_del_gesla(self):
        rezultat = ''
        for i in self.geslo:
            if i in self.crke: #smo uganili
                rezultat += i
            else:
                rezultat += '_'
        return rezultat

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())
# uporabnik poskuša 'uganiti' črko crka
    def ugibaj(self, crka):
        crka = crka.upper()
        if self.poraz():
            return PORAZ

        if crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke += crka
        if self.zmaga():
            return ZMAGA
        if crka in self.geslo:
            return PRAVILNA_CRKA
        if self.poraz():
            return PORAZ
        return NAPACNA_CRKA

bazen_besed = []
with open('besede.txt', encoding='utf8') as input_file:
    bazen_besed = input_file.readlines()


def nova_igra(bazen_besed):
    beseda = random.choice(bazen_besed).strip()

    return Igra(beseda, '')


class Vislice:
    def __init__(self):
        self.igre = {}
    
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
        
    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)

