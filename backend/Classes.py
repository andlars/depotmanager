import datetime
import pickle
import os

ROOT_DIR = os.path.abspath(os.getcwd()) + "\\backend\data\\"

brugerList = []

with open(ROOT_DIR + "BrugerList.pkl", "rb") as unpklBruger:
    brugerList = pickle.load(unpklBruger)

class bruger:
    def __init__(self, admin, brugernavn, bruger_ID, mail):
        self.admin = admin
        self.brugernavn = brugernavn
        self.bruger_ID = bruger_ID
        self.mail = mail

    def write2file(self):
        with open(ROOT_DIR + "BrugerList.pkl", "wb") as pklBruger:
            pickle.dump(brugerList, pklBruger)

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
