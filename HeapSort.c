//heap Sort
#include<stdio.h>
#include<stdlib.h>

void swap(int* a, int* b) 
{ int t = *a; *a = *b;  *b = t; }

void max_heapify(int * A,int i,int n){

	int l,r,largest,temp;
	largest=i;
	l=2*i+1;
	r=2*i+2;
	if((l<n) && (A[l]>A[i]))
	{
		largest=l;
	}
	if((r<n) && (A[r]>A[largest])){
		largest=r;
	}
	if(largest!=i){
		//Exchange the largest and A[i]
		swap(&A[i], &A[largest]);

		max_heapify(A,largest,n);
	}

}
void build_max_heap(int * A, int size){
	int i;

	for(i=(size-1)/2;i>=0;i--){
		max_heapify(A,i,size);
	}
}
void Heap_Sort(int * A,int size){
	//build max heap;

	build_max_heap(A,size);

	while(size>1){
	swap(&A[0], &A[size-1]);
	size--;
	max_heapify(A,0,size);
}

}
int main(){
	int arr[]={4,5,2,6,8,9,6,5,1,0};
	int i;
	int n=sizeof(arr)/sizeof(arr[0]);
	printf("size-%d\n",n );

	Heap_Sort(arr,n);
	
	printf("Sorted  Array \n" );
	for(i=0;i<n;i++){
		printf("%d\n",arr[i]);
	}

return 0;

}