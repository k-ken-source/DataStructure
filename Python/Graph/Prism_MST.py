import sys
# Apply prism MST (Minimum Spanning Tree) algorithm using 2D MATRIX
class Graph:
    def __init__(self,n):
        self.no_of_vertices = n
        self.graph = [[0 for col in range(self.no_of_vertices)] for row in range(self.no_of_vertices)]

    # Utilities 
    def add_edge(self, u,v,w ):
        self.graph[u][v] = w
        self.graph[v][u] = w

    # Print the MST
    def Print(self,parent):
        print("Edge \t Weight")
        for i in range(1,self.no_of_vertices):
            print(parent[i],"-",i,"\t", self.graph[i][parent[i]])
    
    # find the next vertex with smallest shortest distance/ or smallest shortest edge weight

    def FindMinimum(self,distance,visited):
        m = sys.maxsize
        for i in range(self.no_of_vertices):
            if distance[i] <= m and visited[i] ==False: # less than or equalto can change MST we travel through
                m = distance[i]
                index = i
        return index

    # Prism Algorithm
    def Prism(self):
        parent = [0]*self.no_of_vertices
        visited = [False]* self.no_of_vertices
        distance = [sys.maxsize] * self.no_of_vertices
        distance[0] = 0
        parent[0] = None

        # We need to visit all the vertices of the graph 
        for _ in range(self.no_of_vertices):

            u = self.FindMinimum(distance,visited) # Return the index of the edge with smallest weight or distance
            visited[u] = True 
            print("Vertex Picked",u)


            for v in range(self.no_of_vertices):
                # Relax the Edges 
                if self.graph[u][v]>0 and distance[v]>self.graph[u][v] and visited[v]==False:
                    distance[v] = self.graph[u][v]
                    parent[v] = u
        # Print The Minimum Spanning Tree 
        print(distance)
        self.Print(parent)

if __name__ == "__main__":
    n = int(input("Enter the number of vertices"))

    obj = Graph(n)
    e = int(input("Enter the number of edges"))
    for _ in range(e):
        u,v,w = map(int,input().split())
        obj.add_edge(u,v,w)
    obj.Prism()
    

