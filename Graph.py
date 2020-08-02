# implementining Graph with  -
# Adjecency List, Object Oriented Fashion 
from collections import defaultdict

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

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




obj=Graph()

n=int(input("number of Edges"))

for i in range(n):
	u,v=map(int,input().split())

	obj.add_edges(u,v)

s=int(input('source-'))

obj.BFS(s)
