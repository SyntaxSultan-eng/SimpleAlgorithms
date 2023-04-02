from random import randint
import time

N = int(input("What is the length of the array? Enter a number: "))
upper = int(input("The highest bound of the numbers in the array: ")) 
array = []

for _ in range(N):
    array.append(randint(0, upper)) # Creating an array using random int, which acts for the lower and upper bounds of the numbers,
                                    # but lower bounds in this algorithm always  be zero because this algorithm only work with positive numbers

print("This is an unsorted array:")
print(array)

time1 = time.time() # Marking the beginning of the algorithm

#######This is a Radix Sort################

start = 0
maxpazryd = max(array)
length = len(str(maxpazryd))  # We find the number of digits of the max number.

while start < length:
    list = [[] for _ in range(10)]  # creating a two-dimensional array where we will place the digits of units, hundreds, etc.
    for num in array:
        list[int(num / (10**start)) % 10].append(num)  # We put the numbers by digits in [[], [] , ...]
    array.clear()  # clearing the original array to change it in the future
    for bigarray in list:  
        for miniarray  in bigarray:  #We write the modified array to our main array
            array.append(miniarray)
    start += 1

#The main disadvantage of this algorithm is that it sorts only positive numbers

#####End of the algorithm################

time2 = time.time() # Marking the ending of the algorithm
Radix_time = time2 - time1 # finding the running time of the algorithm

print("This is a sorted array:")
print(array)
print("This is the running time of this algorithm:")
print(Radix_time)
        
# This is an algorithm function for easy use in other projects
'''
def RadixSort(array):
    start = 0
    maxpazryd = max(array)
    length = len(str(maxpazryd))  # Кол-во разрядов
    while start < length:
        list = [[] for _ in range(10)]  # единицы, cотни и т.д
        for x in array:
            list[int(x / (10**i)) % 10].append(x)  # Помещаем их в [[], [] , ...]
        array.clear()  # Очищаем
        for x in list:  # Заменить исходную последовательность
            for y in x:  # Чтобы списки извлечь из большого списка [[]] => []
                array.append(y)
        start += 1  
    
    return array
'''
