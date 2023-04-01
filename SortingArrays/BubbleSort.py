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

######This is a BubbleSort###############

length = len(array)
for num in range(length): # We go through each number
    for neighbour in range(num+1, length): # We take the neighbor from num+1 to length
        if array[num] > array[neighbour]: # Compare the numbers in order with their neighbor on the right
            array[num], array[neighbour] = array[neighbour], array[num] # If the right number is smaller, then we will change the numbers

#####End of the algorithm################
    
time2 = time.time() # Marking the ending of the algorithm
bubble_time = time2-time1 # finding the running time of the algorithm

print("This is a sorted array:")
print(array)
print("This is the running time of this algorithm:")
print(bubble_time)

# This is an algorithm function for easy use in other projects
'''
def BubbleSort(array):
    length = len(array)

    for num in range(length):
        for neighbour in range(num+1, length):
            if array[num] > array[neighbour]:
                array[num], array[neighbour] = array[neighbour], array[num]
    
    return array
'''
