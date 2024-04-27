
#grading system 
name=input("enter the name of student ")
maths=int(input("enter maths marks "))
english=int(input("enter english marks "))
python=int(input("enter python marks "))
c=int(input("enter c marks "))
java=int(input("enter java marks "))
t=maths+english+python+c+java
percent=t/5
print("your percentage is: ",percent)
if(maths>100 or english>100 or python>100 or c>100 or java>100 or maths<0 or english<0 or python<0 or c<0 or java<0):
    print("enter the wrong marks criteria")
elif(percent==100):
    print("grade==O")
elif(percent>=90):
    print("grade==A+")
elif(percent>=80):
    print("grade==B+")
elif(percent>=70):
    print("grade==B")
elif(percent>=60):
    print("grade==C")
elif(percent>=50):
    print("grade==D")
else:
    print("fail")

