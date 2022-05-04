from datetime import datetime
from time import sleep, time
from random import random, randint

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
	21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
	41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

# Use for loop to run the code 5 times after every pause amount of time
# Use sleep and randint to generate a time in seconds to pause the program
# for i in range(start, stop{, step})

for i in range(5): 
# Find the time of day and take the minute from that
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
            print("This minute seems a little odd.")
    else:
            print("Not an odd minute.")
# Generate a random integer between 1 and 60, for pause between intervals
#    time.sleep(random.randint(1, 60))
# Best way perhaps, but in order to do the below code, we need to import
# from time and from random both random and randint and sleep and time.
    sleep(randint(1, 60))
#
#   
# The way the book has this seems like creating a variable not needed
#   wait_time = random.randint(1, 60)
#   time.sleep(wait_time)