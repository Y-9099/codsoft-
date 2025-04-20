#NAME-YAMINI THAKRE
#TASK:- CALCULATOR

num1=int(input("ENTER THE FIRST NUMBER:-"))
num2=int(input("ENTER THE SENCOND NUMBER:-"))

print("\n1. ADDITION \n2. SUBRACTION \n3. MULTIPLICATION \n4. DIVISION")

choice=int(input("ENTER THE CHOICES BETWEEN 1-4:"))

if(choice==1):
    print("ADDITION OF TWO NUMBERS",num1 ,"and",num2,"=",num1+num2)

elif(choice==2):
    print("SUBSTRACTION OF TWO NUMBERS",num1 ,"and",num2,"=",num1-num2)


elif(choice==3):
    print("MULTIPLICATION  OF TWO NUMBERS",num1 ,"and",num2,"=",num1*num2)


elif(choice==4):
    print("DIVISION OF TWO NUMBERS",num1 ,"and",num2,"=",num1/num2)