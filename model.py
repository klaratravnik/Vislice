#najprej konstante
import random
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '0'
NAPACNA_CRKA = '-'

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

