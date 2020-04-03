import random
import time

def description():
    print('you are in a playground and you have 2 way go to frindly lion cave or hungry lion cave \n you need to press 1 or 2')

def choosecave():
    print ('which cave do you want to go?? ')
    caveNumber = input()
    return caveNumber

def caveFunction(caveNumber):
    randomNumberCave = random.randint(1,2)
    print('Your Approch is the cave........')
    time.sleep(2)
    print('It\'s dark and spooky')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()    
            
    if randomNumberCave == caveNumber:
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')   
game= "yes"
while game == "yes" or game == "y":
    description()
    time.sleep(2)
    caveNumber = choosecave()
    
    caveFunction(int(caveNumber))
    print()
    print('Do You want Play More game ? Yes // No :')
    game = input()