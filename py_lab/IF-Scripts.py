print ('!!!!!!!!!!!!!!!!!Scripts if!!!!!!!!!!!!!')
Height_MJ = int(input('MJ Height? '))
if Height_MJ >= 190:
    print ('Cerca')
elif Height_MJ >= 150:
    print ('Lejos')
else:
    print ('fallaste')
#for
print ('!!!!!!!!!!!!!Scripts for!!!!!!!!!!!!')
familia = ('Juan', 'Lina', 'Juansimon')
for nombre in familia:
    print (nombre)
for x in range (1,30,3):
    print (x)
#while
print ('!!!!!!!!!!!!!Scripts while!!!!!!!!!!!!')
x = 1
while (x < 10):
    print ('Loop Count is:', x)
    x = x + 1
else:
    print ('loop is finished')


while True:
    string = input('Enter some text to print. \nType "done" to quit>')
    if string == 'done' :
        break
    print (string)
print ('Done!')
