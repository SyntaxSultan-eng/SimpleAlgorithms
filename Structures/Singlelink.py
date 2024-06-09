# This is my implementation of a simple singly linked list

#################### This is simple single linked list #######################
class SingleLinkedList: 
    head = None # Creating a head

    class Node:
        value = None #Our cells only have a value and a link to the next elemen
        next = None 

        def __init__(self, value, next = None): # Initialize them
            self.value = value
            self.next = next

    def append(self, value):
        if self.head is None:
            self.head = self.Node(value) #Checking if our list is empty
            return 
        current = self.head

        while current.next: #We go through the elements of the array and get to the last one
            current = current.next
        
        current.next = self.Node(value) #Adding an element to the array
        return
    
    def out(self):
        if self.head is None:
            print("List is empty") # Checking the length of our array
            return
        current = self.head
        print("[", end="")
        
        while current.next:
            print(current.value, end=",") # We output this array beautifully as a list
            current = current.next

        print(str(current.value) + "]")
        return

# This is simple TEST

list = SingleLinkedList()
list.append(15)
list.append(19)
list.append(-17)
list.out()