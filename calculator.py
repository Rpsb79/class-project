import math
def sum():
    val_1=int(input("enter the number : "))
    val_2=int(input("enter the number : "))
    sum =val_1+val_2
    return sum
def sub():
    val_1=int(input("enter the number : "))
    val_2=int(input("enter the number : "))
    sub =val_1-val_2
    return sub
def mul():
    val_1=int(input("enter the number : "))
    val_2=int(input("enter the number : "))
    mul =val_1*val_2
    return mul
def div():
    val_1=int(input("enter the number : "))
    val_2=int(input("enter the number : "))
    div =val_1/val_2
    return div
def sqrt():
    val_1=int(input("enter the number : "))
    sqrt =math.sqrt(val_1)
    return sqrt
def pow():
    val_1=int(input("enter the number : "))
    val_2=int(input("enter the number : "))
    pow =val_1**val_2
    return pow
def log():
    val_1=int(input("enter the number : "))
    log =math.log(val_1)
    return log
def sin():
    val_1=int(input("enter the number : "))
    sin =math.sin(val_1)
    return sin
def cos():
    val_1=int(input("enter the number : "))
    cos =math.cos(val_1)
    return cos
def tan():
    val_1=int(input("enter the number : "))
    tan =math.tan(val_1)
    return tan
def exp():
    val_1=int(input("enter the number : "))
    
    exp =math.exp(val_1)
    return exp
def fact():
    val_1=int(input("enter the number : "))
    
    fact =math.factorial(val_1)
    return fact
def mod():
    val_1=int(input("enter the number : "))
    val_2=int(input("enter the number : "))
    mod =val_1%val_2
    return mod
def sqr():
    val_1=int(input("enter the number : "))
    sqr =val_1**2
    return sqr
def cube():
    val_1=int(input("enter the number : "))
    cube =val_1**3
    return cube
while True:
    choice=int(input("enter your choice 1->sum 2->sub 3->div 4->mul 5->sqrt 6->pow 7->pow 8->log 9->sin 10->cos 11->tan 12->exp 13->fact 14->mod 15->sqr 16->cube 17->exit:"))
    if choice==1:
       print(sum())
    elif choice==2:
       print(sub())
    elif choice==3:
        print(div())
    elif choice==4:
        print(mul())
    elif choice==5:
        print(sqrt())
    elif choice==6:
        print(pow())
    elif choice==7:
        print(log())
    elif choice==8:
        print(sin())
    elif choice==9:
        print(cos())
    elif choice==10:
        print(tan())
    elif choice==11:
        print(exp())
    elif choice==12:
        print(fact())
    elif choice==13:
        print(mod())
    elif choice==14:
        print(sqr())
    elif choice==15:
        print(cube())
    elif choice==16:
        break
    else:
        print("Invalid choice")
