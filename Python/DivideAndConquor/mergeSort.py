def merge(arr1,arr2):
	L=[]
	i=0
	j=0
	while i<len(arr1) and j<len(arr2):
		if arr1[i]<arr2[j]:
			L.append(arr1[i])
			i+=1
		else:
			L.append(arr2[j])
			j+=1
	while i<len(arr1):
		L.append(arr1[i])
		i+=1
	while j<len(arr2):
		L.append(arr2[j])
		j+=1
	return L

def divide(L):
	if len(L)==1:
		return L

	n=len(L)
	m=n//2
	l=L[:m]
	r=L[m:]

	l=divide(l)
	r=divide(r)

	return merge(l,r)

L=list(map(int,input().split()))
print(divide(L))





