# This is my implementation of a simple Double linked list

###################This is Double linked list ######################
class DoubleList:

    head = None # Creating a head
    tail = None # Creating a tail

    class Node:

        value = None
        next = None #Our cells only have a value,a link to the next element and a link to the previous element
        prev = None
        
        def __init__(self,value, next = None, prev = None):
            self.value = value
            self.next = next   # Initialize them
            self.prev = prev
    
    def append(self,value):
        '''
        If the list is not empty, a new node is created with the given value. 
        This new node is connected to the current tail node by setting the next attribute of the current tail to the new node, 
        and setting the prev attribute of the new node to the current tail. 
        Finally, the tail is updated to point to the new node.
        '''
        if self.head is None:
            self.head = self.tail = self.Node(value) #Checking if our list is empty
            return value
        self.tail.next = self.Node(value)
        self.tail.next.prev = self.tail 
        self.tail = self.tail.next
    
    def out(self):
        '''
        If the list is not empty, it starts from the head and 
        iterates through the list by following the next pointers until it reaches the last node.
        During this iteration, it prints the value of each node followed by a space.
        '''
        if self.head is None:
            print("[]")
            return 
        current = self.head
        while current.next:
            print(current.value, end=" ")
            current = current.next
        print(current.value)
    
    def get(self,index):
        '''
        This method allows you to retrieve the value at a specific index in the doubly linked list
        if the index is within the valid range.
        It starts from the head and 
        iterates through the list by following the next pointers until it reaches the desired node.
        '''
        current = self.head
        counter = 0
        check = True
        while counter < index:
            if not current:
                print("Index out of range")
                check = False
            current = current.next
            counter += 1
        if check:
            print(current.value)

    def rewrite(self,index,value):
        """
        This method allows you to update the value at a specific index in the doubly linked list 
        if the index is within the valid range.
        It starts from the head and 
        iterates through the list by following the next pointers until it reaches the desired node and modifies it.
        """
        current = self.head
        counter = 0
        check = True
        while counter < index:
            if not current:
                print("Index out of range")
                check = False
                break
            current = current.next
            counter += 1
        if check:
            current.value = value
        
    def delete(self,index):
        '''
        This method allows you to delete a node at a specific index from the doubly linked list, 
        handling special cases for deleting the head node.

        1. It starts by checking if the list exists by verifying if the head is None. 
        If it is, it prints "List doesn't exist" and returns.

        2. It then iterates through the list to find the total number of nodes and stores it in the counter variable.

        3. It checks if the specified index is out of range (greater than the total number of nodes or less than 0). 
        If it is, it prints "error" and returns.

        4. If the index is valid, it starts by setting current to the head.

        5. If the index is 0, it handles a special case where the head needs to be updated. 
        If the head has no next node, it simply sets the head to None. 
        Otherwise, it updates the head to its next node and sets the new head's previous pointer to None.

        6. If the index is not 0, it iterates through the list to find the node at the index before the one to be deleted. 
        It then updates the pointers of the nodes before and after the deleted node to skip over the deleted node.
        '''
        if self.head is None:
            print("List doesn't exist")
            return
        
        check = self.head
        counter = 0
        while check.next:
            counter += 1
            check = check.next
        
        if index > counter or index < 0:
            print("error")
            return
        
        current = self.head
        
        if index == 0:
            if self.head.next is None:
                self.head = None
                return
            self.head = self.head.next
            self.head.prev = None
        else:
            for _ in range(index-1):
                current = current.next
            neednum = current.next.next
            if neednum is None:
                current.next = None
            else:
                current.next = neednum
                neednum.prev = current
    
    def add(self,index,value):
        '''
        This method allows you to insert a new node at a specific index in the doubly linked list, 
        handling special cases for inserting at the head position.

        1. It starts by checking if the list exists by verifying if the head is None. 
        If it is, it creates a new node with the specified value and sets it as the head of the list.

        2. It then iterates through the list to find the total number of nodes and stores it in the counter variable.

        3. It checks if the specified index is out of range (greater than the total number of nodes plus one or less than 0). 
        If it is, it prints "error" and returns.

        4. If the index is valid, it starts by setting current to the head.

        5. If the index is 0, it handles a special case where a new head needs to be inserted. 
        It creates a new node with the specified value, sets its next pointer to the current head, 
        and updates the head to point to the new node.

        6. If the index is not 0, it iterates through the list to find the node at the index before 
        the position where the new node should be inserted. 
        It then creates a new node with the specified value and updates the pointers of the nodes before and 
        after the new node to include it in the list.
        '''

        if self.head is None:
            self.head = self.Node(value)
            return value
        
        check = self.head
        counter = 0
        while check.next:
            counter += 1
            check = check.next
        
        if index > counter+1 or index < 0:
            print("error")
            return

        current = self.head
        
        if index == 0:
            self.head = self.Node(value)
            self.head.next = current
        else:
            for _ in range(index-1):
                current = current.next
            previous = current
            neednum = current.next
            current.next = self.Node(value)
            current.next.next = neednum
            current.next.prev = previous
    
    def length(self):
        '''
        This method calculates and prints the length of the doubly linked list by iterating through its nodes and counting them.
        '''

        if self.head is None:
            print(0)
            return
        
        current = self.head
        counter = 1

        while current.next:
            current = current.next
            counter += 1
        print(counter)

            
######################################################


# This is simple test 

list = DoubleList()
list.length()
list.append(12)
list.append(34)
list.append(444)
list.append(26)
list.delete(2)
list.add(0,-23)
list.length()
list.out()
