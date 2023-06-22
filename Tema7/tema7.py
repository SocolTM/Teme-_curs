#Abstraction
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    PI= 3,14
    @abstractmethod
    def aria(self):
        raise NotImplementedError
    @classmethod
    def descriere (cls):
        print('Cel mai probabil am colturi')

#INHERITANCE
#Clasa Pătrat - moștenește FormaGeometrica
#constructor pentru latură

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura
    def aria(self):
        return self.latura * self.latura

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)

# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)

__variabila_private = 'latura'

# getter
def get_variabila_private(self):
    return self.__variabila_private

# setter
def set_variabila_private(self, latura):
    self.__variabila_private = latura

# deleter
def delete_variabila_private(self):
    self.__variabila_private = None

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.raza = raza

    __variabila_private = 'raza'

#getter
    def get_variabila_private(self):
        print(f'Raza cercului este: {self.raza}')
        return self.raza

#setter
    def set_variabila_private(self, raza):
        print(f'Noua valoarea a razei este: {raza}')
        self.raza = raza

#deleter
    def delete_variabila_private(self):
        print(f'Am sters valoarea razei')
        self.raza = 0

#POLYMORPHISM
#Definește o nouă metodă descrie - printează ‘Eu nu am colturi’

    def aria(self):
        aria_cercului = self.PI * self.raza * self.raza
        return aria_cercului
    def descrie(self):
        print(f'Eu nu am colturi')

