//Qucik sORT//
#include<stdio.h>
#include<stdlib.h>
int partition(int arr[],int low,int high)
{
    int i,j,temp,pivot;
    pivot=arr[high];
    i=low-1;
    for(j=low;j<high;j++)
    {
        if(arr[j]<pivot)
        {
            i++;
            temp=arr[j];
            arr[j]=arr[i];
            arr[i]=temp;
            
        }
        
    }
    temp=arr[i+1];
    arr[i+1]=arr[high];
    arr[high]=temp;
    return(i+1);
}

void QucikSort(int arr[],int low,int high)
{
    int pi;
    if(low<high)
    {
    pi=partition(arr,low,high);
    QucikSort(arr,low,pi-1);
    QucikSort(arr,pi+1,high);
    
     
    }
   
}
int main()
{
    int arr[20],n,i;
    printf("enter the size of array");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
        
    }
    QucikSort(arr,0,n-1);
    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
        
    }
    return 0;
    
}
