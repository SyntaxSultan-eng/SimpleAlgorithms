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

time1 = time.time() # Marking the beginning of the algorithm

#######This is a Insertion Sort################

length = len(array)

for num in range(length):
    temp = array[num] 
    neighbor = num - 1
    while neighbor >= 0 and array[neighbor] > temp:  #We consider the first element of the array to be sorted. We work with the unsorted part. 
        array[neighbor+1] = array[neighbor]          #If the neighboring number is smaller, then we insert it into the right place and now it is part of the sorted array.
        neighbor -= 1                                #[5, 6, 1, 3] - [5,[1],6,3] - this case does not fit - [1,5,6,3] and so we do until the full sorting.
        array[neighbor+1] = temp                     #This while loop is responsible for inserting a number in the right place.

#####End of the algorithm################

time2 = time.time() # Marking the ending of the algorithm
Insertion_time = time2 - time1 # finding the running time of the algorithm

print("This is a sorted array:")
print(array)
print("This is the running time of this algorithm:")
print(Insertion_time)
        
# This is an algorithm function for easy use in other projects
'''
def InsertionSort(array):

   length = len(array)

    for num in range(length):
        temp = array[num] 
        neighbor = num - 1
        while neighbor >= 0 and array[neighbor] > temp:   
            array[neighbor+1] = array[neighbor]          
            neighbor -= 1                                
            array[neighbor+1] = temp

    return array

'''