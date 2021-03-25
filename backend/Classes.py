import datetime
import pickle
import os
import random

ROOT_DIR = os.path.abspath(os.getcwd()) + "\\backend\data\\"

brugerList = []

#Pickle og unpickle brugerlisten
with open(ROOT_DIR + "BrugerList.pkl", "wb") as pklBruger:
    pickle.dump(brugerList, pklBruger)

with open(ROOT_DIR + "BrugerList.pkl", "rb") as unpklBruger:
    brugerList = pickle.load(unpklBruger)

#Pickle og unpickle lager
with open(ROOT_DIR + "Lager.pkl", "wb") as pklLager:
    pickle.dump(lager, pklLager)

with open(ROOT_DIR + "Lager.pkl", "rb") as unpklLager:
    lager = pickle.load(unpklLager)


class bruger:
    def __init__(self, admin, brugernavn, bruger_ID, mail):
        self.admin = admin
        self.brugernavn = brugernavn
        self.bruger_ID = bruger_ID
        self.mail = mail

    def write2file(self):
        with open(ROOT_DIR + "BrugerList.pkl", "wb") as pklBruger:
            pickle.dump(brugerList, pklBruger)

def nyBruger():
    global brugerList
    navn = input("Navn:")
    admin = input("True eller False:")
    mail = input("Mail:")
    bruger_ID = random.randint(1000000000000,9999999999999)
    brugerList.append(bruger(admin,navn,bruger_ID,mail))

class vare:
    def __init__(self, varenummer, varenavn, antal):
        self.varenummer = varenummer
        self.varenavn = varenavn
        self.antal = antal

        def formindskAntal(self,n):
            self.antal -= n

        def foroegAntal(self,n):
            self.antal += n

class lager:
    def __init__(self):
        self.vareliste = []
        self.ordrehistorik = []
#        self.dato_for_sidste_optaelling = dato_for_sidste_optaelling
#        self.dato_for_naeste_optaelling = dato_for_naeste_optaelling
#        self.dato = dato

    def tilfoejNyVare(self, varenummer):
        for i in self.vareliste:
            if i.varenummer == varenummer:
                print("Varen eksisterer allerede i systemet")
                return None
        try:
            varenavn = input("Varenavn: ")
            antal = int(input("Antal: "))
            self.vareliste.append(vare(varenummer, varenavn, antal))
        except:
            print("Fejl")

    def fjernEksVare(self, varenummer):
        for i in self.vareliste:
            if i.varenummer == varenummer:
                print("Fjernede " + i.varenavn + " " + str(i.varenummer))
                self.vareliste.remove(i)
                break

class ordre:
    def __init__(self):
        self.vareliste = []
        self.brugernavn = None
        self.bruger_ID = None
        self.tidspunkt = datetime.datetime.now
