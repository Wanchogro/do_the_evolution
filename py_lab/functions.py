# FUNCIONES
def PrintFun():
    '''Prints simple function'''
    print ('Print Function')

PrintFun ()


def sub(arg1, arg2):
    result = arg1 - arg2
    return result

def subparselist(*Args1):
    for arg2 in Args1:
        print ('Hello', arg2, '!')

subparselist ('1', 'hola', '=')
Hello 1 !
Hello hola !
Hello = !



def hello(**k):
    for key, value in k.items():
        print ('Hello', value, '!')

>>> hello (k1='hola', k2='adios', k3='hello',k4='bye')
Hello hola !
Hello adios !
Hello hello !
Hello bye !

def despertador (name, message='Good morning, get up, stand up'):
    print ('Hello', name + ', ' + message)


    despertador ('Juansimon')
    2
