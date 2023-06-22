#exercitiu 1

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

# for i in range(len(masini)):
#     print('Masina mea preferata este:', masini[i])

# for i in masini:
#     print('Masina mea preferata este:',i)
# i=0
# while i < len(masini):
#     print(f'Masina mea preferata este:',masini[i])
#     i +=1
# print('done')

#exercitiu 2

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
#
#
# for i in range(1,len(masini)-1):
#     masini[i]= masini[i].upper()
# else:
#     print(masini)


#exercitiu 3

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

# for masina in masini:
#     if masina == 'Mercedes':
#         print(f'Am gasit masina dorita de dvs: {masina}')
#         break
#     else:
#         print(f'Am gasit masina {masina} .Mai cautam')

#exercitiu 4

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

# for masina in masini:
#    if masina =='Lastun''Trabant':
#        continue
# print(f'S-ar putea să vă placă mașina {masina}')

#exercitiu 5

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat','Trabant', 'Opel']
# masini.remove('Lastun')
# masini.remove('Trabant')
# print(masini)
# masini_vechi=['Lastun','Trabant']
# print(masini_vechi)
# masini_vechi=['Tesla']
# print(masini_vechi)
# masini.extend(masini_vechi)
# print(masini)


#exercitiu 6

# pret_masini = {
# 'Dacia': 6800,
# 'Lastun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
#
# chei=pret_masini.keys()
# print(chei)
# valori=pret_masini.values()
# print(valori)
#
# print(pret_masini.items())

#exercitiu 7

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# i = 0
# for numar in numere:
#     if numar == 3:
#         i = i + 1
# print(f'Numarul 3 apare de {i} ori in lista de numere')

#exercitiul 8

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# s = 0
# for numar in numere:
#     s=s+numar
#     print('Suma numerelor este ', s)

#exerctiu 9

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# max = numere[0]
# for numar in numere:
#     if numar > max:
#         max = numar
# print(f'Cel mai mare numar din lista este: ', max)

#exercitiu 1 optional

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')




#exercitiu optional 3

# import random
#
# numar_secret = random.randint(1, 30)
# numar_ghicit = None
#
# while True:
#     numar_ghicit = int(input("Introduceti numarul: "))
#     if numar_ghicit > numar_secret:
#         print("Numar secret e mai mic.")
#     elif numar_ghicit == numar_secret:
#         print("Felicitări! Ai ghicit!")
#         break
#     else:
#         print("Numar secret e mai mare.")


#exercitiu optional 4

# numar = int(input("Numar dorit: "))
#
# for i in range(1, numar + 1):
#     print(str(i) * i)
