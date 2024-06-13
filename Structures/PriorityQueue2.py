#This is my implementation of a priority queue that deletes by priority

##################### This is PriorityQueue2 #######################################

class PriorityQueue2:
    head = None
    tail = None
    priority = {}
    class Node:
        value = None
        next = None
        prev = None
        # Initialize cells with links on next and previous position and priority
        def __init__(self,value,next = None,prev = None, priority = {}):
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

    def push(self, value):
        '''
        Adds a new node with the given value to the priority queue.
        '''
        if self.head is None:
            self.head = self.tail = self.Node(value)
            return
        self.tail.next = self.Node(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
    
    def out(self):
        '''
        If the queue is not empty, it starts from the head and 
        iterates through the list by following the next pointers until it reaches the last node.
        During this iteration, it prints the value of each node followed by a space.
        '''
        if self.head is None:
            print("Queue is Empty")
            return
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)
        return
    
    def pop(self):
        '''
        Method to remove the element with the highest priority from a priority queue. 
        The code iterates through the queue to find the element with the highest priority and then removes it.
        '''
        if self.head is None:
            print("Queue is Empty")
            return
        current = self.head
        if self.head.next is None:
            self.head = None
            return

        counter = 1
        while True:
            if self.priority[current.value] == counter:
                if current == self.head:
                    if self.head.next is None:
                        self.head = None
                        return
                    self.head = self.head.next
                    self.head.prev = None
                    break
                else:
                    neednum = current.prev
                    if current.next is None:
                        neednum.next = None
                        break
                    else:
                        current.next.prev = neednum
                        neednum.next = current.next
                        break

            if current.next is None:
                current = self.head
                counter += 1
            current = current.next
########################################################    

# This simple PriorityQueue2 (TEST)

list = PriorityQueue2()
print("_______________________")
list.Priority("veteran", 1)
list.Priority("employee", 2)
list.Priority("doctor",3)
list.Priority("normal", 4)
list.push("normal")
list.push("employee")
list.push("veteran")
list.push("doctor")
list.out()
print("_________________________")
list.pop()
list.out()




