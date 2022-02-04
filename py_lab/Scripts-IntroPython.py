#PRINT
Marca_Bicicleta = 'Specialized'
Talla_Bicicleta = 52
print ("MARCA:",Marca_Bicicleta,Talla_Bicicleta)
print (Talla_Bicicleta)
Numero_km = 5*6-1
print (Numero_km)
Largo_pierna = 5//4
print (Largo_pierna)
Talla_Binario = bin(Talla_Bicicleta)
print (Talla_Binario)
Talla_HEX = hex(Talla_Bicicleta)
print (Talla_HEX)
#STRINGS/LISTs/
Marcas_Bicicleta = ['Specialized', 'Trek']
print (Marcas_Bicicleta[1])
Marcas_Bicicleta [1]="Bianchi"
print  (Marcas_Bicicleta[1])
Resumen = [Marca_Bicicleta, Talla_Bicicleta, Talla_HEX]
print (Resumen)
Suma = Resumen + Marcas_Bicicleta
print (Suma[1:3])

#Listas []
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a+b
print (c)
index = c.append('a')
print (c)

d = c.pop(10)
print (d)

#TUPPLE ()
lili = ('ojos', 'nariz', 'cola')
print (lili)
lili_datatype = type (lili)
print (lili_datatype)

In [1]: (a,b,c) = (12, 'Lina', 35)
In [2]: c
Out[2]: 35

#Dictionaries {}
Lina = {"size":(90,60,90), "job":"Teacher", "company":"Gym Fontana"}
type (Lina)
print (Lina)

In [10]: Lina ["address"] = {"Street" : "168", "City" : "Bogota"}
In [11]: Lina

{'size': (90, 60, 90),
 'job': 'Teacher',
 'company': 'Gym Fontana',
 'address': {'Street': '168', 'City': 'Bogota'}}

 #SET {} No Key:Value Pair

In [12]: numbs = {1, 2, 3, 4, 5,6,8,10}
In [13]: odds = {1, 3, 5, 7, 9}

In [14]: type (odds)
Out[14]: set

In [15]: numbs | odds
Out[15]: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

In [18]: numbs & odds
Out[18]: {1, 3, 5}

#input function

In [19]: Nombre = input('su nombre?')
su nombre?Juan

In [20]: Nombre
Out[20]: 'Juan'

In [21]: Nombre = input('su nombre?:')
su nombre?:Juan

In [22]: Nombre
Out[22]: 'Juan'

In [23]: High = float(input('What is your high un meters:'))
What is your high un meters:1.78

In [24]: High
Out[24]: 1.78

In [25]: type(High)
Out[25]: float

In [27]: High = int(input('What is your high un cm:'))
What is your high un cm:179

In [28]: type(High)
Out[28]: int

#Print function

In [29]: print('Hola')
Hola

In [30]: print('Hola\n\nMundo')
Hola

Mundo

In [31]: print('Numbers in set' , 1, ':', numbs )
Numbers in set 1 : {1, 2, 3, 4, 5, 6, 8, 10}

In [32]: print('Numbers in set' , 1, ':', numbs ,sep='')
Numbers in set1:{1, 2, 3, 4, 5, 6, 8, 10}

In [33]: name = 'Pipe'

In [34]: name2 = 'Juan'

In [35]: print (f'{name2} says hello to {name}!')
Juan says hello to Pipe!

# IF CONDITIONAL
n = 20
if n == 20:
    print('correcto!!!')

Height_MJ = float(input('MJ Height? '))

if Height_MJ >= 190:
    print ('Cerca')
elif Height_MJ >= 150:
    print ('Lejos')
else:
    print ('fallaste')
