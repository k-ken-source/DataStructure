from collections import defaultdict
import sys
#Bellman Ford // Shortest Path finding algorithm dealing with negative cycles 
# Slower than dijkstra // Takes O(V.E) time.
#Using A Directed Graph 

class Graph:
    def __init__(self,v):
        self.n = v
        self.graph = defaultdict(list)

    def addEdge(self,u,v,w):
        self.graph[u].append([v,w])
    
    def Print(self,distance):
        print("vertex  distance")
        for i in range(self.n):
            print(i,distance[i])

    def Bellman_Ford(self,src):
        # Initialise 
        distance = [sys.maxsize]*self.n
        distance[src] = 0

        for u in range(self.n):
            for v in self.graph[u]:
                #Relax the edges 
                if distance[u]+v[1] < distance[v[0]]:
                    distance[v[0]] = distance[u]+v[1]

        for u in range(self.n):
            for v in self.graph[u]:
                if distance[u]+v[1] < distance[v[0]]:
                    print("Aborted Negative Cycle shortest path undefined")
                    return
        
        self.Print(distance)

if __name__ == "__main__":
    g = Graph(5)  
    g.addEdge(0, 1, -1)  
    g.addEdge(0, 2, 4)  
    g.addEdge(1, 2, 3)  
    g.addEdge(1, 3, 2)  
    g.addEdge(1, 4, 2)  
    g.addEdge(3, 2, 5)  
    g.addEdge(3, 1, 1)  
    g.addEdge(4, 3, -3)  
    
    g.Bellman_Ford(0) 




