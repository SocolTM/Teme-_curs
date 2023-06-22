# exercitiu1

class Cerc:
    raza = 15
    culoare = 'verde'
    def __init__(self,raza, culoare):
            self.raza = raza
            self.culoare=culoare
    def descrie_cerc(self):
        print(f'Raza cercului este {self.raza} cm si cercul este {self.culoare}')

    def get_aria_cerc(self):
        aria = self.raza * self.raza * 3.14
        return aria
    def get_diametru_cerc(self):
        diametru = self.raza * 2
        return diametru
    def get_circumferinta_cerc(self):
        circumferinta= 2 * 3.14 * self.raza
        return circumferinta

descriere_cerc=Cerc(15,'verde')
print(descriere_cerc.raza)
print(descriere_cerc.culoare)
descriere_cerc.descrie_cerc()

aria_cerc=Cerc(15,'verde')
print(f'Aria cercului este {aria_cerc.get_aria_cerc()} cm')

diametru_cerc=Cerc(15,'verde')
print(f'Diametrul cercului este {diametru_cerc.get_diametru_cerc()} cm')

circumferinta_cerc= Cerc(15, 'verde')
print(f'Circumferinta cercului este {circumferinta_cerc.get_circumferinta_cerc()} cm')

# exercitiul2

class Dreptunghi:
    lungime= 10
    latime = 5
    culoare = 'rosu'
    def __init__(self,lungime,latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare =culoare

    def descrie_dreptunghi(self):
        print(f'Dreptunghiul are lungimea de {self.lungime} cm, latimea de {self.latime} cm si cularea {self.culoare}')


    def get_aria_dreptunghi(self):
        aria = self.lungime * self.latime
        print(f'Aria dreptunghiului este {aria}')

    def get_perimetru_dreptunghi(self):
        perimetru = 2 * self.lungime + 2 * self.latime
        print(f'Perimetrul dreptunghiului este {perimetru}')

descriere_dreptunghi = Dreptunghi(10,5,'rosu')
descriere_dreptunghi = Dreptunghi(10,15,'galben')
descriere_dreptunghi.descrie_dreptunghi()

arie_dreptunghi = Dreptunghi(10,5,'rosu')
arie_dreptunghi.get_aria_dreptunghi()

perimetrul_dreptunghi = Dreptunghi(10,5,'rosu')
perimetrul_dreptunghi.get_perimetru_dreptunghi()

# exercitiu3

class Angajat:
    nume = 'Socol'
    prenume = 'Teodora'
    salar = 2500
#
    def __init__(self, nume, prenume, salar):
        self.nume =nume
        self.prenume = prenume
        self.salar = salar
    def descrie_angajat(self):
        print(f'Ma numesc {self.nume} {self.prenume} cu un salar de {self.salar} lei')

    def nume_complet(self):
        print(f'Numele meu este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul meu pe luna este {self.salar}')

    def salariu_anual(self):
        salariu_anual =0
        salariu_anual= self.salar * 12
        print(f'Salariul meu anual este: {salariu_anual} lei')

    def get_marire_salariu(self):
        marire = 800
        marire_in_procente = (sum({self.salar}, marire))/100
        print(f'Marirea este de {marire_in_procente},%')

descriere_angajat = Angajat('Socol', 'Teodora', 2500)
descriere_angajat.descrie_angajat()

Teodora = Angajat('Socol', 'Teodora', 2500)
Teodora.nume_complet()

salariul_lunar = Angajat('Socol', 'Teodora', 2500)
salariul_lunar.salariu_lunar()

salariul_anual = Angajat('Socol', 'Teodora', 2500)
salariul_anual.salariu_anual()

marirea_salariala = Angajat('Socol', 'Teodora', 2500)
marirea_salariala.get_marire_salariu()

#exercitiu 4

class Cont:
    iban = 123456789
    titular_cont = 'Teodora'
    sold = 3500

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')

    def get_debitare_cont(self):
        debitare_cont = 500
        total_sold = self.sold + debitare_cont
        print(f'Dupa debitare noul sold este de: {total_sold} lei')

    def get_creditare_cont(self):
        creditare_cont = 300
        total_sold = self.sold - creditare_cont
        print(f'Dupa debitare noul sold este de: {total_sold} lei')


afisarea_soldului = Cont(123456789, 'Teodora', 3500)
afisarea_soldului.afisare_sold()

debitarea_contului = Cont(123456789, 'Teodora', 3500)
debitarea_contului.get_debitare_cont()

creditarea_soldului = Cont(123456789, 'Teodora', 3500)
creditarea_soldului.get_creditare_cont()