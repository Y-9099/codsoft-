#NAME-YAMINI THAKRE
#TASK-   ROCK PAPER SCISSOR GAME
import random

ROUNDS=int(input("HOW MANY ROUNDS YOU WANT TO PLAY?:"))#5
user_score=0
computer_score=0
user_total_score=0
computer_total_score=0

for i in range(1,ROUNDS+1):#(1,6)=(1,5)
    choices=["ROCK","PAPER","SCISSOR"]
    user=str(input("CHOOSE BETWEEN ROCK , PAPER, SCISSOR:")) 
    computer=random.choice(choices)
    print("COMPUTER HAS SHOWN:",computer)
    
    if(user==computer):
        print("TIE BETWEEN YOU AND COMPUTER")
        print("YOUR SCORE=",user_score)
        print("COMPUTER's SCORE=",computer_score)

    elif(user=="ROCK" and computer=="PAPER"):
        print("COMPUTER HAS WON")
        computer_score+=1#computer_score=computer_score+1 #0+1=1
        print("COMPUTER's SCORE=",computer_score)
        print("YOUR SCORE=",user_score)#0

    elif(user=="PAPER" and computer=="ROCK"):
        print("YOU WON !!!!!!")
        user_score+=1 #user_score=user_score+1 0+1=1
        print("YOUR SCORE=",user_score)
        print("COMPUTER's SCORE=",computer_score)
    
    elif(user=="ROCK" and computer=="SCISSOR"):
        print("YOU WON")
        user_score+=1
        print("YOUR SCORE=",user_score)
        print("COMPUTER's SCORE=",computer_score)
    
    elif(user=="SCISSOR" and computer=="ROCK"):
        print("COMPUTER HAS WON")
        computer_score+=1
        print("COMPUTER's SCORE=",computer_score)
        print("YOUR SCORE=",user_score)

    elif(user=="SCISSOR" and computer=="PAPER"):
        print("YOU WON!!")
        user_score+=1
        print("YOUR SCORE=",user_score)
        print("COMPUTER's SCORE=",computer_score)

    
    elif(user=="PAPER" and computer=="SCISSOR"):
        print("COMPUTER HAS WON")
        computer_score+=1
        print("COMPUTER's SCORE=",computer_score)
        print("YOUR SCORE=",user_score)
    
    else:
        print("YOU CHOOSED WRONG ! PLAY AGAIN")

    user_total_score=user_total_score+user_score
    computer_total_score=computer_total_score+computer_score
    print("YOUR TOTAL SCORE=",user_total_score)
    print("COMPUTER's TOTAL SCORE=",computer_total_score)
    if(user_total_score>computer_total_score):
        print("YOU WON THE OVERALL GAME")

    elif(computer_total_score>user_total_score):
        print("COMPUTER HAS WON THE OVERALL GAME")

    else:
        print("TIE BETWEEN YOU AND COMPUTER")

    print("GAME OVER")

