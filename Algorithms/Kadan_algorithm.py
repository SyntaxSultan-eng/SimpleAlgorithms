import time
from random import randint

################## Kadan's algorithm ############

def Kadan(nums : list[int]) -> int:
    current_sum = nums[0]
    best_max_sum = nums[0]

    for index in range(1,len(nums)):
        current_sum = max(nums[index], current_sum + nums[index])
        best_max_sum = max(best_max_sum, current_sum)
    return best_max_sum

################################################

def main():
    N = int(input("What is the length of the array? Enter a number: "))
    lower = int(input("The lower bound of the numbers in the array: "))
    upper = int(input("The highest bound of the numbers in the array: "))
    array = []

    for _ in range(N):
        array.append(randint(lower, upper)) # Creating an array using randomint, which asks for the lower and upper bounds of the numbers

    print("This is start array (100 first):")
    print(array[:100])

    time1 = time.time()
    max_sum = Kadan(array)
    time2 = time.time()

    print(f"This is the running time of this algorithm: {time2-time1}")
    print(f"This is max subarray sum: {max_sum}")

################################################

if __name__ == '__main__':
    main()