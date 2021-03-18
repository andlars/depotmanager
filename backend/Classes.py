import datetime

class bruger:
    def __init__(self):
        self.admin = False
        self.brugernavn = ''
        self.bruger_ID = 0
        self.mail = ''

    def nyBruger(self, admin, brugernavn, bruger_ID, mail):
        self.admin = admin
        self.brugernavn = brugernavn
        self.bruger_ID = bruger_ID
        self.mail = mail

    def write2file(self):
        dataString = 'new object type: bruger\n'
        dataString += 'admin: ' + str(self.admin) + '\n'
        dataString += 'brugernavn: ' + self.brugernavn + '\n'
        dataString += 'bruger_ID: ' + str(self.bruger_ID) + '\n'
        dataString += 'mail: ' + self.mail + '\n'
        return dataString

    def readFromFile(self, stringlist):
        adminlist = stringlist[0].split(': ')
        self.admin = adminlist[1].split('\n')[0]
        brugernavnlist = stringlist[1].split(': ')
        self.brugernavn = brugernavnlist[1].split('\n')[0]
        bruger_IDlist = stringlist[2].split(': ')
        self.bruger_ID = bruger_IDlist[1].split('\n')[0]
        maillist = stringlist[3].split(': ')
        self.admin = maillist[1].split('\n')[0]

# Testbrugere
b1 = bruger()
b1.nyBruger(False, 'Kristian Sejr Gotfredsen', 420, 'ksg2001@live.com')
b2 = bruger()
b2.nyBruger(True, 'Nicklas Bogut Nielsen', 69, 'nicklas.bogut@live.dk')
b3 = bruger()
b3.nyBruger(False, 'Simon Marius Mahler Thomsen', 69420, 'simon.thomsen01@gmail.com')

# Indskrivning af testbrugere
file = open('brugerfil.txt', 'w')
file.write(b1.write2file())
file.write(b2.write2file())
file.write(b3.write2file())
file.close()

# readlines
file = open('brugerfil.txt', 'r')
filelines = file.readlines()
for i in range(len(filelines)):
    if filelines[i] == 'new object type: bruger\n':
        b4 = bruger()
        b4.readFromFile(filelines[i+1:i+5])
file.close




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
