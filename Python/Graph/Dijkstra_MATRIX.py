#Goal is to implement dikstra algorithm that would allow you to find the shortest path from source in O(V^2)
#It is being assmed that there are only directed edges with positve weights (No negative cycles) //Condition for dijkstra

#Graph Indexing stats from 1 
import sys 

class Graph:
	def __init__(self,n):
		self.n=n
		self.graph = [[0 for col in range(self.n+1)] for col in range(self.n+1)]

	def add_weighted_edges(self,u,v,w):
		self.graph[u][v]=w

	def initialise(self):
		d={}
		for i in range(1,self.n+1):
			d[i]=False
		return d

	def Print(self,distance):
		print("Vertex\tDistance")
		for i in range(1,self.n+1):
			print(i,"\t",distance[i])
		print()

# SUPPORT FUNCTIONS FOR DIJKSTRA ALGO .......
	def Find_Minimum(self,distance,d):
		m=sys.maxsize
		for i in range(1,self.n+1):
			if distance[i]<m and d[i]==False:
				index = i
				m=distance[i]
		return index

# dijkstra is Iterative, we need to maintain a array to store distance from source
	def Dijkstra(self,s):

		distance = [sys.maxsize]*(self.n+1)
		#initialise the distance from source.....
		distance[s]=0
		d=self.initialise()
		d[0]=True

		# we would need to visit all the vertices starting from s, and /
		# then move forward by obtaining the next vertex with smallest weight distance from source..... 
		for _ in range(self.n):

			u=self.Find_Minimum(distance,d)
#For Debugging: print("Visiting: ",u)
			# Removing the elment from Queue or marking it as visited ....
			d[u]=True
			# Visiting all the vertices nearest to this vertex u 
			for v in range(1,self.n+1):
				# relax all the vertices connected to the the vertex u .....
# For Debugging: print("u",u,"v",v,"distance",distance,"d",d)
				if self.graph[u][v]>0 and (distance[v]> (distance[u]+self.graph[u][v])) and d[v]==False:
					distance[v] = distance[u]+self.graph[u][v]
			
		self.Print(distance)

n=int(input("No of Vertex"))
obj=Graph(n)

e = int(input("Enter number of edges\n"))
print("Enter graph edges with weight in format u v w\n")
for _ in range(e):
	u,v,w=map(int,input().split())
	obj.add_weighted_edges(u,v,w)
s=int(input("Enter source\n"))
obj.Dijkstra(s)
