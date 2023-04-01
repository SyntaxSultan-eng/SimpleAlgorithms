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

length = len(array)
left = 0
right = length

#######This is a Shaker Sort###############

while right > 0:
    for num in range(left,right-1):
        if array[num] > array[num+1]: #This is a bubble sort that goes from left to right
            array[num], array[num+1] = array[num+1], array[num]

    right -= 1 #shifting the right border

    for num in range(right-1,left-1, -1):
        if array[num] > array[num+1]:       #This is a bubble sort that goes from right to left
            array[num], array[num+1] = array[num+1], array[num]

    left += 1 #shifting the left border

#####End of the algorithm################
    
time2 = time.time() # Marking the ending of the algorithm
Shaker_time = time2 - time1 # finding the running time of the algorithm


print("This is a sorted array:")
print(array)
print("This is the running time of this algorithm:")
print(Shaker_time)

# This is an algorithm function for easy use in other projects
'''
def ShakerSort(array):
    length = len(array)
    left = 0
    right = length

    while right > 0:
    for num in range(left,right-1):
        if array[num] > array[num+1]: 
            array[num], array[num+1] = array[num+1], array[num]

    right -= 1

    for num in range(right-1,left-1, -1):
        if array[num] > array[num+1]:      
            array[num], array[num+1] = array[num+1], array[num]

    left += 1

    return array

'''