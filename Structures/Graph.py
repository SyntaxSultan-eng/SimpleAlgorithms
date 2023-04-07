# This is my implementation of a graph with a special method, namely the search for all paths from one vertex to another

############ This is Graph #############################  

class Graph:
    graph = {} # Creating a dictionary in which the key is the vertex and the value is the edges of the graph

    class Node:
        name = None 
        edge = []
    
        def __init__(self,name, edge): # Initialize the name of the vertex and the edges that come out of it
            self.name = name
            self.edge = edge    
            
            
    def add_edge(self, src, dst ):
        if src not in self.graph:  # Creating a vertex
            self.graph[src] = self.Node(src,[])

        if dst is None: # It is our conditional feature that we can create a vertex without edges
            return
        
        if dst not in self.graph :
            self.graph[dst] = self.Node(dst,[]) # src ==> dst  These are vertices so we initialize dst

        self.graph[src].edge.append(dst) # Adding an edge to a graph
        

    def out(self):
        for n in self.graph: #This dumb simple output of graph bindings will be done better in the future (maybe)
           print(self.graph[n].name, '==>', self.graph[n].edge)
  
    

    def path(self, src, dst):
        visited = set()
        paths = [] # all ways
        current_path = [src] # The current path to be used for recursion

        if src not in self.graph or dst not in self.graph :
            print([]) #A kind of panic if we entered the wrong vertices
            return 
 
        def count(src, path): 
            visited.add(src) 
            if src == dst: 
                paths.append(path) # adding a array of the current path to the path list
                visited.remove(src)  # we delete the current vertex from the visited ones to continue the search (if the path was found and we delete the dst so that we can go back to it later if these are not all the paths that we have considered) 
                return 
            for neighbor in self.graph[src].edge: 
                if neighbor not in visited: 
                    count(neighbor, path + [neighbor])
                    current_path.append(neighbor) # recursively calling the function for the next vertex  
            visited.remove(src) # we delete the current vertex from the visited ones to continue the search (After recursion, we delete all the vertices from the set to walk through the graph again) 
 
        count(src, current_path)
        print(paths) 
    
########################################################    

# This simple Graph (TEST)

foo = Graph()
foo.add_edge("a","b")
foo.add_edge("b","c")
foo.add_edge("c","a")
foo.add_edge("c","d")
foo.add_edge("b","d")
foo.add_edge("d","e")
foo.add_edge("f",None)
foo.path("a", "e")
foo.out()