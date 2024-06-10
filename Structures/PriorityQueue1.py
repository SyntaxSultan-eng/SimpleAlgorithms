#This is my implementation of a priority queue that sorts the queue by priority

##################### This is PriorityQueue1 #######################################
class PriorityQueue1:
    head = None
    tail = None
    priority = {}
    class Node:
        value = None
        next = None
        prev = None
        # Initialize cells with links on next and previous position and priority
        def __init__(self,value, next = None, prev = None, priority = {}):
            self.value = value
            self.next = next
            self.prev = prev
            self.priority = priority
    
    def Priority(self,value,num):
        '''
        This is the method that sets the priority. 
        Priority is a dictionary where the word is the key and the number is the priority.    
        '''
        self.priority[value] = num
    
    def pop(self):
        '''
        This method allows you to delete object from queue
        '''
        if self.head is None:
            print("Queue is Empty")
            return
        self.head = self.head.next
    
    def out(self):
        '''
        If the queue is not empty, it starts from the head and 
        iterates through the list by following the next pointers until it reaches the last node.
        During this iteration, it prints the value of each node followed by a space.
        '''
        if self.head is None:
            print("Queue is empty")
            return
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)
        return
    
    def push(self, value):
        '''
        Adds a new node with the given value to the priority queue based on the priority.
        - If the list is empty, it creates a new node and sets it as both the head and tail.
        - Otherwise, it iterates through the list to find the correct position to insert the new node based on its priority.
        - If the new node has higher priority than the current tail, it appends it to the end.
        - If the new node has lower priority than the current head, it inserts it at the beginning.
        - Otherwise, it iterates through the list to find the appropriate position to maintain the priority order.
        '''
        if self.head is None:
            self.head = self.tail = self.Node(value)
            return
        current = self.tail
        if self.head.next is None:
            if self.priority[current.value] <= self.priority[value]:
                    new = self.Node(value)
                    self.tail.next = new
                    new.prev = self.tail
                    self.tail = new
                    self.tail.next = None
                    return
            elif self.priority[current.value] > self.priority[value] :
                new = self.Node(value)
                self.head.prev = new
                new.next = self.head
                new.prev = None
                self.head = new
                self.tail = new.next
                return
        while current.prev:
            if self.priority[current.value] <= self.priority[value]:
                if current == self.tail:
                    new = self.Node(value)
                    self.tail.next = new
                    new.prev = self.tail
                    self.tail = new
                    self.tail.next = None
                    break
                else:
                    previous = current
                    neednum = current.next
                    current.next = self.Node(value)
                    current.next.next = neednum
                    current.next.prev = previous
                    break
            current = current.prev
        if current == self.head:
            if self.priority[current.value] > self.priority[value]:
                new = self.Node(value)
                self.head.prev = new
                new.next = self.head
                new.prev = None
                self.head = new
                self.tail = new.next
            else:
                previous = current
                neednum = current.next
                current.next = self.Node(value)
                current.next.next = neednum
                current.next.prev = previous
########################################################    

# This simple PriorityQueue1 (TEST)


list = PriorityQueue1()
print("__________________")
list.Priority("veteran",1)
list.Priority("employee",2)
list.Priority("peopbyappoint",3)
list.Priority("normal",4)

list.push("employee")
list.push("veteran")
list.push("normal")
list.push("peopbyappoint")
list.push("peopbyappoint")
list.push("normal")
list.push("veteran")

list.out()
list.pop()
print("_________________")
list.out()