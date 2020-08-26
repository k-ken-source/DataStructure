#include<stdio.h>
#include<stdlib.h>
#define range 200


int main(){
	int *pos = (int *)calloc(range,sizeof(int));
	int *out = (int *)calloc(range,sizeof(int));


	int n,i,size;
	size=n;


	printf("Enter the numbers to enter\n");
	scanf("%d",&n);
	int * arr = (int *)malloc(n*sizeof(int));
	for(i=0;i<n;i++){
	scanf("%d",&arr[i]);
	pos[arr[i]]+=1;
}

for (i = 1; i <= range; ++i) 
        pos[i] += pos[i-1];

for(i=0;i<n;i++){
	out[pos[arr[i]]]=arr[i];
	pos[i]+=1;
}

for(i=0;i<n;i++){
	printf("%d ",arr[i]);
}

return 0;
}