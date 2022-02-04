#Script de pruebas y laboratorios de Cisco DEVASC Chap3_PythonBasics
print("hello world")
#
for kids in ["Juan", "Lina", "Simon"]:
    print("Vamos al parque,", kids, ":)")

'''Hola
    Linea 2
        Linea 3'''

#Data Types and Variables
print(hex(18374))

print(int('1')+1)
    #String
a='JuanCamilo'
print(a[0:4])
print(a[:4])
print(a[2:])
print(a[-2:])
print(a[:-2])
print('Juan' + 'Camilo')
print('Juan'*4)
print(str.lower(a))
    #List
nombres = [a, (a[0:4]+ 'Simon'), 'Linita']
print(nombres)
print (nombres[2])
routers = ['rt1', 'rt2', 'rt3']
switch = ['sw1' ,'sw2', 'sw3']
netdevices = routers + switch
print(netdevices)
rt1 = list.count(netdevices, 'rt1')
print(rt1)
    #Tuples
vendors = ('Cisco', 'F5', 10, 'HP')
print (type(vendors))
    #Dictionaries
sw1 = {"CPU": (98,78,80), "process": "stp"}
print(sw1["CPU"])
sw1["memory"] = {"Process":"stp", "buffer":"0"}
print(sw1)
print(sw1["memory"])
#sets
numbs = {1, 2, 4, 5, 6, 8, 10}
odds = {1, 3, 5, 7, 9}
print(numbs | odds)
print(numbs & odds)
#inputs&Outputs
name = input('Ingrese su nombre: ')
print(name)
temp = float(input('What is the temperature in C: '))
print(temp)
print('Hello\nWorld')
print('Numbers in set', 1, ':', numbs )
print('Numbers in set ', 1, ': ', numbs, sep='' )
food1 = 'platano'
food2 = 'pollo'
print(f'{food1} asado con {food2}')
#Conditional loops IF
n = 20
if n == 20:
    print ('The number is 20')
cpu = int(input('What was the cpu % ?:'))
if cpu >= 90:
    print('CPU is OK')
elif cpu >= 80:
    print('CPU is RISING')
elif cpu >= 70:
    print('CPU is DANGER')
elif cpu >= 60:
    print('CPU is WARNING')
else:
    print('CPU is FINE')
#Conditional loops for
list_devices = ('192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4')
for devices in list_devices:
    print(devices)
for x in range(3):
    print(x)
for x in range(1,89,4):
    print(x)
#Conditional loops for
count = 1
while (count < 5):
    print ("La cuenta va en: ", count)
    count = count + 1
else:
    print("Se acabo esta vaina")
while True:
    valor = input('Enter some text to print. \nType "salir" to quit> ')
    if valor == 'salir' :
        break
    print(valor)
print('Fin!')



    