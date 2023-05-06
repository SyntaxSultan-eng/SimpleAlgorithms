from random import randint
import time

N = int(input("What is the length of the array? Enter a number: "))
lower = int(input("The lower bound of the numbers in the array: "))
upper = int(input("The highest bound of the numbers in the array: "))
array = []

for _ in range(N):
    array.append(randint(lower, upper)) # Creating an array using randomint, which asks for the lower and upper bounds of the numbers

print("This is an unsorted array:")
print(array)

######################This is QuickSort #######################

def QuickSort(array):
    if len(array) <= 1: #If we have an array length less than 1, then we return this array (a condition for recursion)
        return array
    
    main = array[0] # I take the first element as the main one to compare with it

    less = [x for x in array[1:] if x <= main]  # array with numbers smaller than the main one
    greater = [x for x in array[1:] if x > main] # array with numbers bigger than the main one

    return QuickSort(less) + [main] + QuickSort(greater) # The main thing in quick sorting is recursion. We find our own less and greater for each array (less and greater).

####################### End of the algorithm ####################

time1 = time.time()# Marking the beginning of the algorithm

array = QuickSort(array)

time2 = time.time() # Marking the ending of the algorithm

Quick_time = time2 - time1 # finding the running time of the algorithm

print("This is a sorted array:")
print(array)
print("This is the running time of this algorithm:")
print(Quick_time)







