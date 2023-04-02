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

#######This is a Selection Sort################

length = len(array)

for num in range(length):
    min = num
    for neighbor in range(num, length):   # In the first iteration, we look for the minimum number in the array and change it with the first, 
        if array[min] > array[neighbor]:  # then we look for the local minimum now without the first number and change it with the second, etc. 
            min = neighbor                # We do this until the array is sorted.
    array[num], array[min] = array[min], array[num]

#####End of the algorithm################

time2 = time.time() # Marking the ending of the algorithm
Selection_time = time2 - time1 # finding the running time of the algorithm

print("This is a sorted array:")
print(array)
print("This is the running time of this algorithm:")
print(Selection_time)
        
# This is an algorithm function for easy use in other projects
'''
def SelectionSort(array):
    length = len(array)

    for num in range(length):
        min = num
        for neighbor in range(num, length):
            if array[min] > array[neighbor]:
                min = neighbor
        array[num], array[min] = array[min], array[num]
    
    return array
'''