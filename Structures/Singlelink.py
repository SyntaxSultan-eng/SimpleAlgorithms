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

    def lenght(self) -> int:
        '''
        Output the length of a singly linked list
        '''
        if self.head is None:
            return 0
        
        counter = 1 #Counted the head element
        current = self.head

        while current.next: #We go through the elements of the array and get to the last one
            current = current.next
            counter += 1
        return counter
    
    def get(self, index: int) -> int:
        '''
        Outputs the element by index
        '''
        if index < 0 or index >= self.lenght():
            return -1
        if index == 0:
            return self.head.value
        
        current = self.head
        counter = 1 #Counted the head element
        
        while current.next:
            if counter == index:
                return current.next.value # Get the element
            current = current.next
            counter += 1
    
    def addAtHead(self, val: int) -> None:
        '''
        Adding an element to the head
        '''
        if self.head is None:
            self.head = self.Node(val) #Checking if our list is empty
            return
        
        current = self.Node(val) #Making a new element - head
        current.next = self.head 
        self.head = current
        return

    def append(self, value: int) -> None:
        '''
        Adding an element to the tail
        '''
        if self.head is None:
            self.head = self.Node(value) #Checking if our list is empty
            return 
        current = self.head

        while current.next: #We go through the elements of the array and get to the last one
            current = current.next
        
        current.next = self.Node(value) #Adding an element to the array
        return
    
    def addAtIndex(self, index: int, val: int) -> None:
        '''
        Adding an element by index
        '''
        if index < 0 or index > self.lenght():
            return -1
        if index == 0:
            if self.head is None:
                self.head = self.Node(val) # Create linked list
                return
            self.addAtHead(val) #Adding an element to the head
            return
        counter = 1
        current = self.head
    
        while current.next:
            if counter == index:
                last_current = current.next
                current.next = self.Node(val) #Adding an element
                current.next.next = last_current
                return
            counter += 1
            current = current.next
        
        # If the index points to the last element
        last_current = current.next
        current.next = self.Node(val) 
        current.next.next = last_current

    def deleteAtIndex(self, index: int) -> None:
        '''
        Deleting an element by index
        '''
        if index < 0 or index >= self.lenght():
            return
        if index == 0:
            self.head = self.head.next
            return
        
        counter = 1
        current = self.head
    
        while current.next:
            if counter == index:
                current.next = current.next.next #Just changing the binding of the elements
                return
            counter += 1
            current = current.next
        
    def out(self) -> None:
        '''
        Output this array beautifully as a list
        '''
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
    
###########################################

# This is simple TEST

list = SingleLinkedList()
list.addAtHead(7)
list.addAtHead(2)
list.addAtHead(1)
list.addAtIndex(3,0)
list.deleteAtIndex(2)
list.addAtHead(4)
list.append(4)
list.out()
print(list.get(4))
list.addAtHead(4)
list.addAtIndex(5,0)
list.addAtHead(6)
list.out()
