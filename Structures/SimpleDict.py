# This is my Dictionary implementation for python
# The dictionary is based on array and cells with a value and a key

#################This is Simple Dictionary####################
class dictionary:
    dict = []
    class Node:
        key = None
        value = None
        def __init__(self,key,value): # This is array and cell initialization with key and value
            self.key = key
            self.value = value
        
    def add(self, key,value): # Add function
        for x in self.dict:
            if x.key == key: # The main property of a dictionary is that there are no identical keys
                return
        self.dict.append(self.Node(key,value))# add element

    def get(self, key): # Function to get an element from a dictionary
        check = False
        for x in self.dict:   
            if x.key == key: # iterate through the dictionary and output the element
                print(x.value)
                return
        if not check: # if the element not in dictionary
            print("Key error")
    
    def rewrite(self, key, value): # key rewriting function
        check = False
        for x in self.dict:
            if x.key == key: # iterate through the dictionary and change the element
                x.value = value
                return
        if not check: # if the element not in dictionary
            print("Key error")

############################################################################

# This is simple test:
dict = dictionary()
dict.add(1,"sad")
dict.get(1)
dict.rewrite(1,"alo")
dict.get(1)
        
