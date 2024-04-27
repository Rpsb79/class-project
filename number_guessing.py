
#guessing number game
import random as p

a=int(input("enter the number "))
b=p.randrange(1,a)
c=int(input("enter the number "))
while(True):
    if(c==0):
        print("game over,player quite the game.")
        break
    elif(c==b):
        print("congratulation you are right. the random number was:",c)
        break
    elif(c<b):
        c=int(input("you are near to correct it play some more time"))
    elif(c>b):
        c=int(input("your guessing is around to corect please play more time"))
    else:
        c=int(input("try again"))
        
