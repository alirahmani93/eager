"""
In this document we want to guess the number that has already been assumed.
If the guess is correct, it returns the congratulatory text, and if it is wrong,
it deducts one star from us.
"""
class seprator:
    def dash():  print("_"*5)        # Only for sepration lines
    def straline(): print("*"*stars) # Represents the remaining number of stars
from random import *
# Random Generate stras
luck = int(input("Number of your LUCK: "))

ran  = random()+1.0
rand = int(ran*100)
stars = int(luck*rand/(luck + rand))
if stars >15: stars =5                # stars LIMIT
print("Your Sky has {0} Star(s).".format(stars))
# Random generate assumed
assumed= int((rand /(2*stars)))

# Status announcement
def Tips(assumed,guess): 
    answer = (print("Make a bigger guess") if assumed>guess
              else print("Make a lower guess"))
    return answer

while stars>0:
    guess= float(input("Pick a number: "))    
    if guess!=assumed:
        stars-=1
        seprator.dash()
        Tips(assumed,guess)
        seprator.dash()
        print ("You LOSE")
        seprator.straline()
    else:
        print("You WON")
        
    print("There Is No STAR In The SKY.") if stars == 0 else print(("{} Star(s) Remine").format(stars))


print("assumed is:", assumed) # REAL ANSWER


