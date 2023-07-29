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

#######This is a Merge Sort################    

def Merge_sort(left, right):

    i = 0
    j = 0
    answer = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            answer.append(left[i]) # we check the numbers and merge them
            i += 1
        else:
            answer.append(right[j])
            j += 1
    while i < len(left):
        answer.append(left[i])
        i += 1
    while j < len(right):
        answer.append(right[j])
        j += 1
    return answer


def Splitting(array):
    if len(array) == 1: # simple check
        return array

    centre = len(array) // 2 # take the center of the list
    left = Splitting(array[:centre])  #Our first step is to split the list in two
    right = Splitting(array[centre:])

    return Merge_sort(left, right) # recursively dividing arrays

##### End of the algorithm ################

time1 = time.time() # Marking the beginning of the algorithm

sort_array = Splitting(array) # Main Function 

time2 = time.time() # Marking the ending of the algorithm

MergeTime = time2 - time1 # finding the running time of the algorithm

print("This is a sorted array:")
print(sort_array)
print("This is the running time of this algorithm:")
print(MergeTime)
