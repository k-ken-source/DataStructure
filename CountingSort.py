
#Assume the range to be 200 
RAN=200
# creating a index based frequency array; 

pos=[0 for _ in range(RAN)]
out=[0 for _ in range(RAN)]
A=[]


print("Enter the number to enter")
n=int(input())
some=n
for i in range(n):
	inp=int(input())
	A.append(inp)
	pos[A[i]]+=1

i = RAN-1

while i>=0:
	pos[i]=n-pos[i]
	n=pos[i]
	i-=1


for i in A:
	out[pos[i]]=i
	pos[i]+=1

for i in range(some):
	print(out[i],end=" ")