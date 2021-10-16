"""
we want make DICE
"""

from random import *

num= int(input("give me a number: "))

def luck(num): 
    luck=0
    while luck not in range(1,7,1):
        luck=0
        a=int(random() *num)
        luck+=a
        #print (a,luck)
    return luck



Dice = print(luck(num))
