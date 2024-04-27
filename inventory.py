
inventory={}
while True:
    a= input("enter what want you to do? add, remove, display,quit: ")
    if a=='add':
        i=input("enter item name: ")
        q=int(input("enter your quantity: "))
        if i in inventory:
            inventory[i]+=q
        else:
            inventory[i]=q
    elif a=='remove':
        i=input("enter the name of item you want to remove: ")
        q=int(input("enter the quantity you want to remove: "))
        if i in inventory and inventory[i]>=q:
            inventory[i]-=q
        elif i in inventory and inventory[i]<q:
            print("There are only {inventory[item]} left in {item} left in inventory.")
        else:
            print(f"ther is no item left in inventory.")
    
    elif a=='display':
        print("Inventory")
        for key,value in inventory.items():
            print(f"{key}:{value}")
    
    elif a =='quit':
        break
    else:
        print("invalid entry please try again. ")
