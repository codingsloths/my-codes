#############################################################
# Jenna Summers
# 12/6/21
# Programming Assignment 1 - How Many Zeros?
#############################################################
#Import Time Library
from time import time

#User Input
maxRange = int(input("What number do you want to count to zeros to? "))

#Setting Variable Names
number = 0
count = 0

#Start Time:
start_time = time()

#Function that Returns the Count
def count_zeros(number):
    return str(number).count('0')

#For loop that iterates through all numbers, finding the zeros.
for i in range(1, maxRange + 1):
    number = number + 1
    count = count + count_zeros(number)
    if number == maxRange:
      print("The number of zeros written from 1 to {} is {}. " .format(maxRange, count))

#End Time
elapsed = time() - start_time

#Print Statement
print("This took {} seconds.".format(elapsed))

#So the file doesn't close out before it finishes
input("press ENTER to exit")




