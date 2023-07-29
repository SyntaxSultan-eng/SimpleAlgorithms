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

######This is a HeapSort###############

def pyramid(array, n, i):
    head = i
    left = (2 * i) + 1
    right = (2 * i) + 2
    if left < n and array[left] > array[head]: #we are building a pyramid so that parents greater children
        head = left # changing elements
    if right < n and array[right] > array[head]:
        head = right # changing elements
    if head != i:
        array[i], array[head] = array[head], array[i]
        pyramid(array, n, head) # recursively we continue to build the pyramid


def HeapSort(array):
    length = len(array)

    for i in range(length, -1, -1):  # building a pyramid
        pyramid(array, length, i)

    for i in range(length - 1, 0, -1):  # sort by changing the first and last
        array[0], array[i] = array[i], array[0]
        pyramid(array, i, 0)
    return array

#####End of the algorithm################

time1 = time.time() # Marking the beginning of the algorithm

sort_array = HeapSort(array) # Main Function 

time2 = time.time() # Marking the ending of the algorithm

HeapTime = time2 - time1 # finding the running time of the algorithm

print("This is a sorted array:")
print(sort_array)
print("This is the running time of this algorithm:")
print(HeapTime)
