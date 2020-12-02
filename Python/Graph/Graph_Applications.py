from collections import defaultdict 

# Grapg node indexing starts at index 1 

class Graph:
	def __init__(self):
		self.graph=defaultdict(list)

		self.cycle=[]

	def add_edges_directed(self,u,v):
		self.graph[u].append(v)

	def add_edges_Undirected(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def Cycle_Util_Undirected(self,s,visited,parent):
		for v in self.graph[s]:
			if visited[v]==False:
				visited[v]=True
				if self.Cycle_Util_Undirected(v,visited,s):
					return True
			elif v!=parent:
				return True

		return False 

	def Cycle_Detection_Undirected(self,n):

		visited = [False]*(n+1)	
		for s in list(self.graph.keys()):
			if visited[s]==False:
				visited[s]=True
				if self.Cycle_Util_Undirected(s,visited,-1):
					return True
		return False

	def Cycle_detection_Directed(self,n):
		visited=[False]*(n+1)
		recStack=[False]*(n+1)

		for s in list(self.graph.keys()):
			if self.Cycle_Util_Directed(s,visited,recStack):
				return True
		return False


	def Cycle_Util_Directed(self,s,visited,recStack):
		visited[s]=True
		recStack[s]=True

		for v in self.graph[s]:
			if visited[v]==False:
				if self.Cycle_Util_Directed(v,visited,recStack):
					self.cycle.append(v)
					return True
			elif recStack[v]==True:
				self.cycle.append(v)
				return True
		
		recStack[s]=False
		return False

# Used to solve job sheduling problems // Requirement- Given that graph must not have any cycle or there wont be a solution
# Applied on DAC ( Directed Acyclic Grapgh )
# Vertices Represents task and Edges represents Dependencies 
	def DFS(self,s, visited,order):
		visited[s]=True
		for v in self.graph[s]:
			if not visited[s]:
				DFS(v,visited,order)
		
		order.insert(0,s)

	def Topological_Sort(self,n):
		visited =[False]*(n+1)
		order=[]
		for s in range(1,n+1):
			if not visited[s]:
				self.DFS(s,visited,order)
		print(order)


obj=Graph()

n=int(input("number of Edges"))

for i in range(n):
	u,v=map(int,input().split())

	obj.add_edges_directed(u,v)

if obj.Cycle_detection_Directed(n):
	print('Found Cycle')
	print(obj.cycle)
else:
	print('Not found')
print(obj.graph)
obj.Topological_Sort(n)

