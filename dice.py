
#roll the  dice
import random as r
a=1
s=p=0
while(a<7):
    b=r.randint(1,6)
    c=int(input("enter the number between 1to 6: "))
    choice=input("if you quite type'quite' otherwise type 'no' : ")
    s+=b
    p+=c
    if(choice=='quite'):
        break
    elif(choice=='no'):
        continue
    else:
        print("wrong choice")
        break
        
print("\n")
print("your score is:",p)
print("the computer score is:",s)
print("\n")
if(s>p):
    print("computer won with score of:",s)
else:
    print("you won with the score of:",p)
