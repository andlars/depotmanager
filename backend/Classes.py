import datetime

class bruger:
    def __init__(self,admin, brugernavn, bruger_ID, mail):
        self.admin = admin
        self.brugernavn = brugernavn
        self.bruger_ID = bruger_ID
        self.mail = mail

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
    def __init__(self, dato_for_sidste_optaelling, dato_for_naeste_optaelling, dato):
        self.vareliste = []
        self.ordrehistorik = []
        self.dato_for_sidste_optaelling = dato_for_sidste_optaelling
        self.dato_for_naeste_optaelling = dato_for_naeste_optaelling
        self.dato = dato

class ordre:
    def __init__(self):
        self.vareliste = []
        self.brugernavn = None
        self.bruder_ID = None
        self.tidspunkt = datetime.datetime.now
