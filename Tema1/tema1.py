#exercitiul 2
#variabila string = un rand de caractere delimitate de ""

#exercitiul 4

 #string
marca_accesoriu ='Cartier'
model_accesoriu = 'lantisor'
print(f'Am vazut la magazin un:  {model_accesoriu}')
print(f'este {marca_accesoriu}')

#integer
dimensiune_lantisor = 60
print(dimensiune_lantisor)

#float
pret = 2850.70
print(pret)

#boolean
original = False
print(original)

#exercitiul 3 curs drive
accesoriu = 'Cartier'
print('accesoriu este un lantisor',type(accesoriu))
lantisor=60
print('lantisorul are dimensiunea de', type(lantisor))
pret = 2850.70
print('pretul lantisorului este de', type(pret))
original = False
print('din pacate este un exemplar', type(original))

#exerciciul 4 drive
pret=2850.70
print(round(pret))

#exercitiul 5 drive

accesoriu = 'Cartier'
lantisor=60
pret = 2850.70
original = False
print(f'Acest lantisor este un {accesoriu}, are dimensiunea {lantisor} cm si este la pretul de {pret} insa este un exemplar {original}')

#exercitiul 6
nume= input('Socol')
prenume= input('Teodora')
print('numele complet are', len('nume+prenume'),'caractere')

#exercitiul 7
lungimea = int(input('lungime'))
latimea = int(input('latime'))
print('Aria dreptunghiului este',int(latimea*lungimea))

#exercitiul 8 si 9
string_example = 'Coral is either the stupidest animal or the smartest rock'
print(string_example.count('the'))

#exercitiul 10
a='Coral is either the stupidest animal or the smartest rock'
assert a=='Coral is either the stupidest animal or the smartest rock'
print('acest string nu contine numere')

#exercitiu 6 - tema Andreea
numere = 'de la', 1, 'la', 20
for i in range (1, 20, 3) :
    print(f'{i}')

#exercitii optionale

#exercitiul 1
i= input('Notare: ')
for index in range (len(i)) :
    if(index % 2 != 0):
      print(i[index])
x = len(i)
y = x // 2
print('Caracterul din mijloc este:', i[y])

#exercitiul 2
#palindrom = functia care returneaza inversul unui string.

a = 'blablabla'
assert a !=1, 'a nu este palindrom'
print('a nu este palindrom')

#exercitiu 3
a= 'alabala portocala'
input('introduceti string a')
print('Ai introdus alabala portocala')

#alabala p o r t o c a l a
1234567891011121314151617
print(a[0:8])
print(a[8:18])

#exercitiu 4
a= 'alabala portocala'
input('introduceti string a')
print('Ai introdus alabala portocala')
print(a[0])
b='lalalalalala'
print(b[0])

a= 'alabala portocala'
a = a[0:1].lower() + a[1:len(a)-1].upper() + a[len(a)-1:len(a)].lower()
print(a)
