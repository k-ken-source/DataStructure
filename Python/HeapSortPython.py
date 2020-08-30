#Heap Sort 
class Build_Heap(object):
	def __init__(self,A,size):
		self.A=A
		self.size=size

	def max_heap(self,i):
		largest=self.i
		l=2*self.i+1
		r=2*self.i+2
		if l<self.size and self.A[l]>self.A[largest]:
			largest=l
		if r<self.size and self.A[r]>self.A[largest]:
			largest=r
		if largest!=self.i:
			A[self.i],A[largest]=A[largest],A[self.i]

			max_heap(largest)

def build_max_heap(A):
	size=len(A)
	n=size//2
	while n>=0:
		max_heap(A,n,size)
		n-=1
	print(A)

def Heap_Sort(A):
	build_max_heap(A)

	size=len(A)
	for i in range(size-1,0,-1):
		A[0],A[i]=A[i],A[0]
		max_heap(A,0,i)
		
print("Enter the elements of array")

A=list(map(int,input().split()))
Heap_Sort(A)
print(A)

