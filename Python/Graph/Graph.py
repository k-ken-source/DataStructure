# implementining Graph with  -
# Adjecency List, Object Oriented Fashion 
from collections import defaultdict

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)
		self.parent ={}

	def add_edges(self,u,v):
		self.graph[u].append(v)
	
	def BFS(self,s):
		visited=[False] * len(self.graph)
		queue=[s]
		visited[s]=True

		while queue:
			s=queue.pop(0)
			print(s)

			for i in self.graph[s]:
				if visited[i]==False:
					visited[i] = True
					queue.append(i)
	
	def bfs_erik_style(self,s):
		level ={s:0}
		parent={s:None}
		queue = [s]
		i=1

		while queue:
			next_queue=[]

			for u in queue:
				for v in self.graph[u]:
					if v not in level:
						level[v]=i
						parent[v]=u
						next_queue.append(v)
			queue=next_queue
			i+=1
		print(level)
		print(parent)

#Allows You to Visit All the Nodes of a graph once, in a depth first manner // Can be utilised in solving many problems. 
	def DFS_visit(self,s):
		for v in self.graph[s]:
			if v not in self.parent:
				self.parent[v]=True
				self.DFS_visit(v)

	def DFS(self):
		for s in list(self.graph.keys()):
			if s not in self.parent:
				self.parent[s]=True
				self.DFS_visit(s)
		print("ALL NODES THAT ARE VISITED - ",list(self.parent.keys()))



if __name__=='__main__':
	obj=Graph()

	n=int(input("number of Edges"))

	for i in range(n):
		u,v=map(int,input().split())

		obj.add_edges(u,v)

	obj.DFS()
	#s=int(input('source-'))

	#obj.bfs_erik_style(s)
