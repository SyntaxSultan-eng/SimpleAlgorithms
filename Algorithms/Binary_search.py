from random import randint  
import time

############## Binary search #####################

def Binary_search(nums : list[int], target : int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right-left) // 2  # Calculate the middle index
        if nums[mid] == target:           # If the target is found, return the index
            return mid
        elif nums[mid] < target:          # If target is greater, ignore the left half
            left = mid + 1
        else:                             # If target is smaller, ignore the right half
            right = mid - 1
    return -1

################################################

def main():
    N = int(input("What is the length of the array? Enter a number: "))
    lower = int(input("The lower bound of the numbers in the array: "))
    upper = int(input("The highest bound of the numbers in the array: "))
    array = []

    for _ in range(N):
        array.append(randint(lower, upper)) # Creating an array using randomint, which asks for the lower and upper bounds of the numbers
    array.sort() # Binary search works correctly only with sorted array

    print("This is start array:")
    print(array)

    target = int(input("Enter the target "))
    
    time1 = time.time() # Marking the beginning of the algorithm
    answer = Binary_search(array,target)
    time2 = time.time() # Marking the ending of the algorithm

    print(f"This is the target index: {answer}")
    print(f"This is the running time of this algorithm: {time2-time1}")

################################################

if __name__ == "__main__":
    main()
