#NAME-YAMINI THAKRE
#TASK-PASSWORD GENERATOR
import random
length=int(input("ENTER THE DESIRED PASSWORD LENGTH:"))
characters="abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password=""

for i in range(1,length+1):
    password+=random.choice(characters)

    print("YOUR PASSWORD :",password)