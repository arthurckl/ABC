# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:17:13 2015

@author: Arthur
"""

import random
import time
a = 0    #pontos do computador
b = 0    #pontos do usuário
A = ["rock","paper", "scissors", "lizard", "spock"]
     
print ("Let's play a game! Rock, paper, scissors, spock and lizard!")     
time.sleep(1.5)
     
computer_choice = random.choice(A)
    
while a < 3 or b< 3:
    print("a %d b %d" %(a,b))
    user_choice = str(input("Choose between rock, paper, scissors, lizard and spock: "))

    computer_choice = random.choice(A)
    if a == 2 and b == 1:
        a = a - 2 
        b = b -1 
    if a == 1 and b == 2:
        a = a - 1 
        b = b - 2 
    if a == 1 and b == 1:
        a = a - 1
        b = b - 1
    if a == 3 and b == 0:
        print ("I won the game,play again") 
        a = a - 3
    if a==0 and b == 3:
        print ("You won the game!!Play again")
        b = b - 3
    if user_choice == "rock" and computer_choice == "rock":
        print ("It's a draw") 
        a==a  and b==b
    elif user_choice == "scissors" and computer_choice == "scissors":
        print ("It's a draw")
        a==a and b==b
    elif user_choice == "paper" and computer_choice == "paper":
        print ("It's a draw")
        a==a and b==b
    elif user_choice == "spock" and computer_choice == "spock":
        print ("It's a draw")
        a==a and b==b
    elif user_choice== "lizard" and computer_choice == "lizard":
        print ("It's a draw") 
        a==a and b==b
    elif user_choice == "rock" and computer_choice == "paper":
        print ("I won")  
        a += 1
        print ("I chose paper" )
    elif user_choice == "paper" and computer_choice == "rock":
        print ("You won")
        b += 1
        print ("I chose rock")
    elif user_choice == "scissors" and computer_choice == "paper":
        print ("You won")
        b += 1
        print ("I chose paper")
    elif user_choice == "paper" and computer_choice == "scissors":
        print ("I won")
        a += 1
        print ("I chose scissors")
    elif user_choice == "lizard" and computer_choice == "paper":
        print ("You won")
        b += 1
        print ("I chose paper")
    elif user_choice == "paper" and computer_choice == "lizard":
        print ("I won")
        a += 1
        print ("I chose lizard")
    elif user_choice == "spock" and computer_choice == "paper":
        print ("I won")
        a += 1
        print ("I chose paper")
    elif user_choice == "paper" and computer_choice == "spock":
        print ("You won")  
        b += 1
        print ("I chose spock")
    elif user_choice == "rock" and computer_choice == "scissors":
        print ("You won") 
        b += 1
        print ("I chose scissors")
    elif user_choice == "scissors" and computer_choice == "rock":
        print ("I won")
        a += 1
        print ("I chose rock")
    elif user_choice == "scissors" and computer_choice == "spock":
        print ("I won")
        a += 1
        print ("I chose spock")
    elif user_choice == "spock" and computer_choice == "scissors":
        print ("You won") 
        b += 1
        print ("I chose scissors")
    elif user_choice == "scissors" and computer_choice == "lizard":
        print ("You won")
        b += 1
        print ("I chose lizard")
    elif user_choice == "lizard" and computer_choice == "scissors":
        print ("I won")
        a += 1
        print ("I chose scissors")
    elif user_choice == "rock" and computer_choice == "spock":
        print ("I won")
        a += 1
        print ("I chose spock")
    elif user_choice == "spock" and computer_choice == "rock":
        print ("You won")
        b += 1
        print ("I chose rock")
    elif user_choice == "rock" and computer_choice == "lizard":
        print ("You won")
        b += 1
        print ("I chose lizard")
    elif user_choice == "lizard" and computer_choice == "rock":
        print ("I won")  
        a +=1
        print ("I chose rock ")
    elif user_choice == "lizard" and computer_choice == "spock":
        print ("You won")
        b += 1
        print ("I chose spock")
    elif user_choice == "spock" and computer_choice == "lizard":
        print ("I won")
        a += 1
        print ("I chose lizard")
    else:
        print ("try again")
        