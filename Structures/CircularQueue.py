#Our convention is that the next tail link is the head, and the previous head link is the tail
#Another condition that pop is the transfer of the head to the end of the queue (to the tail)

####################This is a circular queue########################

class Queue:

    head = None #creating a head and tail for convenience
    tail = None

    class Node:
        value = None
        next = None # Initialize the value, the reference to the next element and the previous one
        prev = None
        def __init__(self,value, next = None, prev = None):
            self.value = value
            self.next = next
            self.prev = None

    def push(self, value): 
        if self.head is None: #If the queue is empty, then add the first element - the head and tail of the queue
            self.head = self.tail = self.Node(value)
            return
        self.tail.next = self.Node(value)
        self.tail.next.prev = self.tail  #If we already have items in the queue, then we shift the tail and add
        self.tail = self.tail.next

    def pop(self):
        if self.head is None: #if there are no items in the queue, then we output an error
            print("Queue is empty!")
            return
        if self.head.next is None: # If there is one item in the queue, then we do nothing
            return
        current = self.head
        self.head = self.head.next #This is my implementation of the transfer
        self.tail.next = current
        current.prev = self.tail
        self.tail = current
        self.tail.next = None
    
    def get(self,index):
        self.head.prev = self.tail # This is our main condition
        self.tail.next = self.head # This is our main condition

        if index == 0:
            print(self.head.value) # if the index is 0 then we return the head
            return
        if index > 0:
            counter = 0
            current = self.head # If the index is positive, then we start from the head and go counterclockwise
            while counter < index:
                current = current.next 
                counter += 1
            print(current.value)
            return
        if index < 0:
            counter = 0
            current = self.tail
            while counter > index: # If the index is negative , then we start from the tail and go clockwise
                current = current.prev
                index += 1
            print(current.value)
            return
    def out(self):
        if self.head is None:
            print("Queue is empty")
            return
        current = self.head
        while current.next != self.head: # We output the values until we meet the head again
            print(current.value, end = " ")
            current = current.next
        print(current.value)

# This is Simple CircularQueue (TEST)       
            
list = Queue()
list.push(12)
list.push(-334)
list.push(313)
list.pop()
list.get(12)
list.get(0)
list.out()
