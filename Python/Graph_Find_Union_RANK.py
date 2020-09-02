#Another Cycle detection algorithm that improves Find Union Using DataStructure Augmentation
#Idea is to reduce the time complexity of Find Operation to O(Lg(n))

#Inherits from Graph.py from same directory 
from Graph import Graph as Parent 

# we define a datastructure that stores the parent of a Vertex and rank of the vertex::
#Initially Vertices are their own parents and their rank is 0
#We Will This DataStructure - Vertex

class Vertex(object):
    def __init__(self,vertex):
        self.parent = vertex
        self.rank = 0

#indexing for graph is kept (0 to n) for now 
class Find_PathCompression(Parent):
    def __init__(self,n):
        Parent.__init__(self)
        self.no_of_vertex=n

    def Find(self,arr,x):
        if arr[x].parent == x:
            return x
        return self.Find(arr,arr[x].parent)
    
    def Union(self,arr,x,y):
        if arr[x].rank > arr[y].rank:
            arr[y].parent = x

        elif arr[x].rank < arr[y].rank:
            arr[x].parent = y
        
        else:
            arr[y].parent = x
            arr[y].rank+=1

    def FindCycle(self):
        # first we intialise a SET of Vertex Element 
        SET=[]
        for vertex in range(self.no_of_vertex):
            SET.append(Vertex(vertex))

        for u in self.graph.keys():
            for v in self.graph[u]:
                x = self.Find(SET,u)
                y = self.Find(SET,v)
                if x==y:
                    return True
                self.Union(SET,x,y)
        return False
if __name__ == '__main__':
    obj = Find_PathCompression(int(input("Enter the number of vertices ")))
    edges = int(input("Enter the number of edges (u,v)"))
    for _ in range(edges):
        u,v = map(int,input().split())
        obj.add_edges(u,v)
    
    if obj.FindCycle():
        print("Found Cycle")
    else:
        print("No Cycle")
