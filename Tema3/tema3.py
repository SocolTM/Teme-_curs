# #exercitiu 1
# punctul a
# note_muzicale= ['do','re','mi','fa','sol','la','si','do']
# print(note_muzicale)
#punctul b
# note_muzicale= ['do','re','mi','fa','sol','la','si','do']
# print('note_muzicale[7] =', note_muzicale[::-1])
# #punctul c

# print('note_muzicale[7] =', note_muzicale[::1])

#exercitiu 2

# note_muzicale= ['do','re','mi','fa','sol','la','si','do']
# print(len(note_muzicale[::7]))

#exercitiu 3

# lista1=[3, 1, 0, 2]
# lista2=[6, 5, 4]
# #
#varianta 1
#  lista1.append(lista2)
#  print(lista1)
#
# varianta 2
# lista1.extend(lista2)
# print(lista1)

#exercitiu 4

# lista1=[3, 1, 0, 2]
# lista2=[6, 5, 4]
# lista1.extend(lista2)
# print(lista1)
# lista1.sort()
# print(lista1)
# lista1.remove(0)
# print(lista1)

#exercitiu 5

# lista3=[0,1,2,3,4,5,6]
# if lista3>=[len(lista3)]or lista3<=[]:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')
#exercitiul 6

# lista1.clear()
# print(lista1)

#exercitiu 7

# lista3=[]
# if lista3>=[len(lista3)]or lista3<=[]:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')


#exercitiu 8
#
# dict1 = {'Ana' : 8,
#          'Gigel' : 10,
#          'Dorel' : 5
# }
# chei=dict1.keys()
# print(chei)
#
# #exercitiu 9
#
# dict1 = {'Ana' : 8,
#          'Gigel' : 10,
#          'Dorel' : 5
# }
# print('Ana a luat nota',{8})
# print('Gigel a luat nota', {10})
# print('Dorel a luat nota', {5})

#exercitiu 10

# dict1['Dorel']= 6
# print(dict1)

#exercitiu 11

# dict1 = {'Ana' : 8,
#          'Gigel' : 10,
#          'Dorel' : 5
# }

# dict1.pop('Gigel')
# dict1.update({'Ionica':9})
# print(dict1)

#exercitiu 12

# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica','luni'}
# print(zile_sapt)
#nu a recunoscut elementul adaugat, mi-a adus doar o singura data ziua de luni

#exercitiu 13

# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
#
# if zile_sapt.intersection(weekend) :
#    print(True)
# else:
#    print(False)

#exercitiu 14

# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
#
#  x=zile_sapt-weekend
#  print('diferenta este ', x)
#
# x= weekend-zile_sapt
# print('diferenta este', x)

#exercitiu 15

# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}

# x= zile_sapt.intersection(weekend)
# print(x)

#exercitiu optional
#Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
lista_jucatori_teren=['1','2','3','4','5']
lista_jucatori_rezerva=['6','7','8','9','10']
lista_jucatori_scosi= []
#
# SCHIMBARI_MAX= 3

lista_jucatori_teren.count('lista_jucatori_teren')
print(lista_jucatori_teren)
