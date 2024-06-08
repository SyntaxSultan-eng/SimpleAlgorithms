class PriorityQueue1:
    head = None
    tail = None
    priority = {}
    class Node:
        value = None
        next = None
        prev = None
        
        def __init__(self,value, next = None, prev = None, priority = {}):
            self.value = value
            self.next = next
            self.prev = prev
            self.priority = priority
    
    def Priority(self,value,num):
        self.priority[value] = num
    
    def pop(self):
        if self.head is None:
            print("Queue is Empty")
            return
        self.head = self.head.next
    
    def out(self):
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