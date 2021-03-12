class bruger:
    def __init__(self,admin, brugernavn, bruger_ID, mail):
        self.admin = admin
        self.brugernavn = brugernavn
        self.bruger_ID = bruger_ID
        self.mail = mail

class lager:
    def __init__(self, dato_for_sidste_optaelling, dato_for_naeste_optaelling, dato):
        self.dato_for_sidste_optaelling = dato_for_sidste_optaelling
        self.dato_for_naeste_optaelling = dato_for_naeste_optaelling
        self.dato = dato
