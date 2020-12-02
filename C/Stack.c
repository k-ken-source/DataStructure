//Stack Implementation

#include<stdlib.h>
#include<stdio.h>

struct node {
	int data;
	struct node* next;
};
struct node * top=NULL;

void push(int data)
{
	struct node * newNode=(struct node *)malloc(sizeof(struct node));
	newNode->data=data;

	if(top==NULL){
		newNode->next=NULL;
		top=newNode;
		return;
	}

	newNode->next=top;
	top=newNode;
	return;
}
void pop(){
	struct node * temp=top;
	if(top==NULL){
		printf("UnderFlow");
		return;
	}

	top=top->next;
	free(temp);
	return;
}
void printList(){
	struct node * temp=top;
	while(temp!=NULL){
		printf("->%d",temp->data);
		temp=temp->next;
	}

}

int main(){
	int data,n,i;
	printf("Enter the number of elemenets to be push");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&data);
		push(data);
	}

	printList();
	printf("\n");
	pop();
	printList();
	
	return 0;
}