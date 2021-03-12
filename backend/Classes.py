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
