# MST - Minimum Spanning Tree 
# The idea is sort the graph according to its weight and then add the minimum weighted//
# edge to the MST

#######  COMPLEXITY OF KRUSKAL - O(Elog(E)) or O(Elog(V)) as E=V^2   /////

class Vertex:
    def __init__(self,vertex):
        self.parent=vertex
        self.rank=0

class Graph(object):
    def __init__(self,no_of_vertices):
        self.no_of_vertices = no_of_vertices
        self.graph = []
        self.parent=[]

    def add_edges(self,u,v,w):
        self.graph.append([u,v,w])
    
    def Find(self,SET,u):
        if SET[u].parent == u:
            return u
        return self.Find(SET,SET[u].parent)
    
    def Union(self,arr,x,y):
        if arr[x].rank>arr[y].rank:
            arr[y].parent = x
        
        elif arr[x].rank<arr[y].rank:
            arr[x].parent = y
        
        else:
            arr[y].parent = x
            arr[y].rank+=1
        
    def Kruskal(self):
        SET=[]
        for i in range(self.no_of_vertices):
            SET.append(Vertex(i))
        
        self.graph = sorted(self.graph,key=lambda x: x[2])

#OBSERVATION        
# If there are n vertices in the graph then are going to be n-1 edges in the MST
        e=self.no_of_vertices-1
        i=0
        while e: 

            u,v,w = self.graph[i]
            i+=1

            x = self.Find(SET,u)
            y = self.Find(SET,v)

            if x!=y:
                self.Union(SET,x,y)
                print("Edge Added :", u,"->",v, "weight",w)
                e-=1
        
if __name__=='__main__':
    n=int(input("Enter the no of vertices"))
    obj=Graph(n)
    e = int(input("Enter the number of edges"))
    
    for _ in range(e):
        u,v,w = map(int,input().split())
        obj.add_edges(u,v,w)
    obj.Kruskal()

