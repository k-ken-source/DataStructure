#Need to find Cycle in a Graph using Disjoint set FOR UNDIRECTED GRAPH //Find and Union
from Graph import Graph 
#Inherits from Graph.py from same folder
class UnionAndFind(Graph):
    def __init__(self):
        Graph.__init__(self)        
    
    def Find(self,parent,x):
        if parent[x]==-1:
            return x
        return self.Find(parent,parent[x])

    def Union(self,parent,x,y):
        parent[x]=y

    def Find_Cycle(self,no_of_edges):
        
        parent=[-1]*(no_of_edges)

        for u in self.graph.keys():
            for v in self.graph[u]:
                print("Edge = ","u",u,"v",v)
                x=self.Find(parent,u)
                y=self.Find(parent,v)
                print("x",x,"y",y)
                if x==y:
                    return True
                self.Union(parent,x,y)
        return False
if __name__=='__main__':
    obj=UnionAndFind()
    n=int(input("Enter the number of Vertex"))
    for _ in range(int(input("No of edges"))):
        u,v=map(int,input().split())
        obj.add_edges(u,v)

    if obj.Find_Cycle(n):
        print("Found Cycle")
    else:
        print("No Cycle")




