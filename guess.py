import random

print('What is your Name?')
name= input()
chance = 0 
print('Wellcome Mr. '+name)

randomNumber = random.randint(1,10)

for chance in range(4):
    print('Guess a Number from 1 to 10 :')
    number = int(input())
    chance +=1

    if number>randomNumber:
        print('Your Guess is high number')
    elif number < randomNumber:
        print('Your guess is low number')
    else:
        print('your guess is correct')
        print('congratulation !! '+ name + ' you anser is correct you take '+ str(chance) +' times')
        break


if number != randomNumber:
    print('Sorry !!! You Lose the game. Correct Anser Is '+ str(randomNumber))