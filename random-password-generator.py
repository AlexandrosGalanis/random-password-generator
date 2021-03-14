#Alexandros Galanis icsd14027
import random

passlist = []
while True:
    print("if you want to close the program press 0 else press a key to continue")
    inputexit = input('Press a key: ')
    
    if inputexit == "0":
        print("The passwords you made: ")
        print (passlist)
        print("Bye!!")
        break


    inputcolor = input('Give me your favorite color: ')
    inputpet = input('Give me the name of your pet: ')
    inputnumber = input('Give me your favorite number: ')
    inputduck = input('Give me the name of your duck: ')
    passwordlenght = int(input('Give me the lenght of the password you wish to have: '))

    password =''
    for i in range (passwordlenght):#for every character of the password we are gonna choose differend fields etc.favorite color,pet,number...
        randomField = random.randint(1,4)#and after we get a random field we are gonna add a random letter of his favorite random field expect
        
        if randomField==1:#if this is the number, in that case we put the number in that spot
            password += random.choice(inputcolor)
        elif randomField==2:
            password += random.choice(inputpet)
        elif randomField==3:
            password += inputnumber
        else:
            password += random.choice(inputduck)
        
    print(password)
    passlist.append(str(password))
    #print (passlist)
