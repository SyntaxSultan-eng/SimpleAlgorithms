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
rightside = length

#######This is a Comb Sort################

while rightside > 1:
    rightside -= 1
    for num in range(length - rightside):   #Sorting is based on bubble sorting,
        endnum = num + rightside            # but we go from the beginning and from the end to the center comparing numbers.
        if array[num] > array[endnum]:      # You can improve sorting by using the golden ratio
            array[num], array[endnum] = array[endnum], array[num]

#####End of the algorithm################

time2 = time.time() # Marking the ending of the algorithm
Comb_time = time2 - time1 # finding the running time of the algorithm

print("This is a sorted array:")
print(array)
print("This is the running time of this algorithm:")
print(Comb_time)
        

