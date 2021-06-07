def generate(tx,ty,n):
	X=[-1,1,-2,2,-2,2,-1,1]
	Y=[-2,-2,-1,-1,1,1,2,2]
	res=[]
	for i in range(8):
		x=tx+X[i]
		y=ty+Y[i]

		if x<1 or x>n or y<1 or y>n:
			continue
		res.append((x,y))
	return res

def BFS(x,y,tx,ty,n):
	i=1
	visited=[[False]*(n+1) for _ in range(n+1)]
	visited[x][y]=True
	queue = [(x,y)]
	while queue:
		new=[]
		for u in queue:
			for v in generate(u[0],u[1],n):
				if v==(tx,ty):
					return(i)
				if visited[v[0]][v[1]]==False:
					visited[v[0]][v[1]]=True
					new.append(v)
		i+=1
		queue=new
		#print(queue)

	#print(visited)
	return -1

t=int(input())
for _ in range(t):
	n=int(input())
	x,y= map(int,input().split())
	tx,ty = map(int,input().split())
	if (x,y)==(tx,ty):
		print(0)
	else:
		print(BFS(x,y,tx,ty,n))
