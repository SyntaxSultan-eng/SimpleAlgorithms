#This is my implementation of a simple queue, where the first one is deleted and the addition occurs at the end (LILO - last in last out)

########################### This is Queue ###########################

class Queue:
    
    head = None #creating a head and tail for convenience
    tail = None

    class Node:
        value = None
        next = None  # Initialize the value, the reference to the next element and the previous one
        prev = None
        def __init__(self,value, next = None, prev = None):
            self.value = value
            self.next = next
            self.prev = prev

    def push(self,value):
        if self.head is None: #If the queue is empty, then add the first element - the head and tail of the queue
            self.head = self.tail = self.Node(value)
            return value
        self.tail.next = self.Node(value)
        self.tail.next.prev = self.tail  #If we already have items in the queue, then we shift the tail and add
        self.tail = self.tail.next

    def pop(self):
        if self.head is None:
            print("Queue is empty") #We remove the first element by shifting the head to the right
            return
        self.head = self.head.next

    def out(self):
        if self.head is None:
            print("Queue is empty") #The output of the elements is quite simple we just go through the links starting from the head and output the elements
            return
        current = self.head  
        while current.next:
            print(current.value, end= " ")
            current = current.next
        print(current.value)

###################################################################

# This is Simple test

list = Queue()
list.push(1)
list.push(2)
list.pop()
list.push(3)
list.push(4)
list.pop()
list.out()

# The most difficult thing is to understand the links how they work and how to use them correctly