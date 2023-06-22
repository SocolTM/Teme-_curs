# #exercitiul 1

# def suma_numere(x):
#      numar1= 5
#      numar2= 8
#      for numar in x:
#           return 5+8
#
# print(suma_numere('numar1,numar2'))
#
# #exercitiul 2
#
# def numere_pare_impare():
#     number = int(7)
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# x = numere_pare_impare()
# print(x)

#exercitiul 3

# def nr_litere_nume(nume, prenume, nume_mijlociu):
#                 return len(nume+prenume+nume_mijlociu)
# print(nr_litere_nume('Socol', 'Teodora', 'Maria'))

#exercitiu 4

# lungime=10
# latime=5
# def aria_dreptunghiului(x):
#     return latime * lungime
# for i in 'x':
#     result = aria_dreptunghiului(i)
#     print('Aria lui',i, '=',result)

# exercitiu 5
# def aria_cercului(r):
#     PI = 3.14
#     r=20
#     return PI * (r*r)
# print("Aria cercului= %.f" % aria_cercului(20))

#exercitiu 6

# def cautare_caracter(string, x):
#     if x in string:
#         return True
#     else:
#         return False
#
# print(cautare_caracter('alabalaportocala', 'a'))
# print(cautare_caracter('alabalaportocala', 'i'))

#exercitiu 7

# def calculator_de_litere(text):
#     upper_case=0
#     lower_case=0
#     for litera in text:
#         if litera.isupper()== True:
#             upper_case += 1
#         elif litera.islower() ==True:
#             lower_case += 1
#     print(f'Textul a fost {text}')
#     print(f'Numarul de litere mici este {lower_case}')
#     print(f'Numarul de litere mari este {upper_case}')
#
# txt_tastatura = input('Introduceti un text :')
# calculator_de_litere(txt_tastatura)
# calculator_de_litere('Am 3 ani')

#exercitiul 8
# lista_numere = [3,5,18,22, -3,-8]
# def numere_pozitive(numere):
#     lista_numere_pozitive = []
#     for numar in numere:
#         if numar > 0:
#             lista_numere_pozitive.append(numar)
#     return lista_numere_pozitive
# print(numere_pozitive(lista_numere))

#exercitiu9

# def doua_numere(x, y):
#     if x == y:
#         print(f'Numerele sunt egale')
#     elif x > y:
#         print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
#     else:
#         print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
#
# doua_numere(48, -2)
# doua_numere(16, 70)

#exercitiul10

# set_numere_input = {4,3,15,-4,21}
# set_numere_input = {4,3,15,-4,21}

# def adaugare_numar(set_numere, numar_nou):
#     if numar_nou in set_numere:
#         print(f'nu am adaugat numarul {numar_nou} in set, exista deja')
#         return False
#     else:
#         set_numere.add(numar_nou)
#         print(f'am adaugat numarul {numar_nou} in set')
#         return True
# print(adaugare_numar(set_numere_input, 21))
# print(adaugare_numar(set_numere_input, 17))