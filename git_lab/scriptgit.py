#Platzi: Flujo de trabajo Git.
#Chapter 4 - Functions
def devnet():
    '''prints simple function'''
    print('Simple function')


devnet()
#
def cpu_rt():
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


cpu_rt()
#
def sub(arg1, arg2) :
    result = arg1 - arg2
    return result
    
print(sub(arg1=10, arg2=8))

#Python allows you to use * and ** (often referred to as *args and **kwargs) to define any number of arguments or keyword arguments. * and ** allow you to iterate through a list or other collection of data,
def hola(*args):
    for arg in args:
        print ("Hola", arg, "!")

hola ('Juan','Linita', 'Simon')
#By using keyword arguments, you can send a list of key/value pairs to a function

def adios(**kwargs):
    for key, value in kwargs.items():
        print("Adios y suerte", value, "!")

adios(kwargs1='Juan', kwargs2='Linita', kwargs3='Simon')
#You can also supply a default value argument in case you have an empty value to send to a function.
def eoldevices(hostname, message='Check inventory'):
    print ('El siguiente equipo', hostname + ':' + message)

eoldevices('rt1')
eoldevices('rt2', 'Revisar con ingenieria')


def dnac_devices(hostname, message='In DNAC'):
    print ('El siguiente equipo', hostname + ':' + message)

dnac_devices('RouterWAN1')
dnac_devices('RouterWAN2', 'Check ARGUS DB')
dnac_devices('RouterWAN3', 'no Liveness ')
dnac_devices('NEXUS ACI', 'Controled')
dnac_devices('INFOBLOX', 'not managed')
dnac_devices('Switch', 'not categorized')
dnac_devices('WLC', 'not categorized')

