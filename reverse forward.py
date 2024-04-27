#reverse forward row,column printing
st=int(input("enter the starting point "))
en=int(input("enter the end point "))
up=int(input("enter the updation "))

choice=input("enter your choice for forward printing or reverse printing:")
choice2=input("enter the choice for row printing or column printing:")

if choice=="forward":
    if choice2=="row":
        for i in range(st,en,up):
            print(i,end=',')
    elif choice2=="column":
        for i in range(st,en,up):
            print(i)
    else:
        print("enter valid choice.")
elif choice=="reverse":
    if choice2=="row":
        for i in range(en,st,-up):
            print(i,end=',')
    elif choice2=="column":
        for i in range(en,st,-up):
            print(i)
    else:
        print("enter valid choice")
else:
    print("your both choices are wrong")
