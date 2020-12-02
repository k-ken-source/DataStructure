from collections import defaultdict
# Prism MST algorithm using HeapExtraction(Log(n)) maing the algorith O(Elog(E))
class Node(self):
    def __init__(self,v,w):
        self.v = v
        self.weight = w

class Heap(self):
    def __init__(self,n):
        self.heap=[]
        self.size=n

    def MinHepify(self,index):

        left = 2*index +1
        right = 2*index +2
        largest = index

        if left< self.size and self.heap[left] < self.heap[largest]:
            largest = left
        
        if right < self.size and self.heap[right] < self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[largest],self.heap[index] = self.heap[index],self.heap[largest]
            self.MinHepify(largest)
    
    def extractMin(self):
        #exchange min element with the last -> decrese size of heap -> call minheapify for the 0th index
        if self.size == 0:
            return
        
        # exchanges 0th index and last index of heap
        temp = self.heap[0]
        self.heap[0] = self.heap[self.size-1]

        self.size -=1

        self.MinHepify(0)
        return temp
    
    class Graph:
        def __init__(self,v):
            self.v = v
            self.graph = defaultdict(list)

        def add_edges(self,u,v,w):
            obj = Node(v,w)
            self.graph[u].append(obj)

            obj1 = Node(u,w)
            self.graph(v).append(obj1)

        def Prism(self):
            parent =[]
            #create heap 
            
            for _ in range(self.v):

                u = 

