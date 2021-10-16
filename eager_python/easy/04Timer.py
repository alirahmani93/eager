import time
import os 

sec = int(input("TIME is: "))
minute = int(input("TIME is: "))*60
hour = int(input("TIME is: "))*3600


print('Start')
time.sleep(sec+minute+hour)
print ('Finish')
