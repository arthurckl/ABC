# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:27 2015

@author: Arthur

Game Rock-Paper-Scissors-Spock-Lizard:
With the old rules of Rock-Paper-Scissors, but now there are
two more options, Spock and Lizard.
"""
import random

A = ["rock","paper","scissors","spock","lizard"]

B = {"rock":["paper","lizard","spock","scissors"],
     "paper":["scissors","rock","lizard","spock"],
"scissors":["rock","paper","spock","lizard"],
"lizard":["rock","spock","scissors","paper"],
"spock":["lizard","rock","paper","scissors"]};
     
answer = str(input(("Hello!, how about we play Rock-Paper-Scissors-Spock-Lizard?\n"+
      "If you want to, type 'yes', if not... type 'no'\n" +
      "Anytime you want to quit in the middle of the game, just type 'quit'\n"))).lower()
def decision(answer):
    if answer == "yes":
        print("Alright! Let's play! \n Good Luck champs")    
        return True 
    elif answer == "no":
        print ("Ok then, bye")
        return False
    else:
        print("Type correctly please, I didn't understand")
        answer = str(input("*"))
        return decision(answer)
w = decision(answer)
while w == True:
    user_point = 0
    computer_point = 0
    while user_point != 3 or computer_point != 3:
        if user_point == 3 or computer_point == 3:
            break
        else:
            user_choice = str(input("Your turn:")).lower()
            computer_choice = random.choice(A)
            if user_choice == computer_choice:
                user_point == 0 and computer_point == 0
                print("It's a draw")
            elif user_choice in A:
                for key,value in B.items():
                    for i in range(len(value)):
                        if user_choice == key and value[i] == computer_choice:
                            if i % 2 == 0:
                                computer_point += 1
                                print ("I won this round,%s beats %s" % (computer_choice,
                                                                         user_choice))
                                if user_point > 0:
                                    user_point -= 1
                            else:
                                user_point += 1
                                print ("You won this round,%s beats %s" % (user_choice,
                                                                           computer_choice))
                                if computer_point > 0:
                                    computer_point -= 1
                print("Your points:",user_point,"\nComputer points:",computer_point)
            else:
                print("There's no option for such thing!Choose correctly this time.")
    if user_point == 3:
        print("You win!Very Good!")
    else:
        print("You lose!What a loser haha!") 
    x = str(input("Do you want to play again? \n"+
                  "Type 'yes' if you want to, or 'no' if you don't want to \n")).lower()
    if x == "yes":
        print("Again?! Great!")
        w = True
    else:
        w = False
        print("See you later!")

        