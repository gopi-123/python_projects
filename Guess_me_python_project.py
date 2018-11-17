#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:45:25 2018

@author: gopinath
"""

# Guess me Project - Similar to rolling a dice problem and guessing the number


 

  #import random module
import random as a
#a is an alias to module random
  
#get input from the user 
#type cast "string input" to integer value
guess= int(input("Please enter your guessing number between 1 to 2 \n"))

#print("your guess number:", guess)


#generate a random nubmer from 1 until 2
game_hidden_num= a.randint(1,2)
  
#print("game* num:" ,game_hidden_num)
#check whether it is right or wrong

#print("type(guess):",type(guess))
#print("type(game_num)", type(game_num))


if (guess==game_hidden_num): 
    print(" Congrats! you guessed it right")
else:
    print("Sorry your guess was not right")