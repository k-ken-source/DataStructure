#include<stdio.h>
#include<stdlib.h>

struct node{
	int data;
	struct node* next;
};

struct node *head;

void insert_beg(int data)
{
	
		struct node *newNode = (struct node *)malloc(sizeof(struct node));
		newNode->data=data;

		if(head == NULL){
			newNode->next=NULL;
			head=newNode;
		}
		else{
			newNode->next=head;
			head=newNode;
		}
}

void inset_end(int data){
	struct node * newNode= (struct node *)malloc(sizeof(struct node));
	newNode->data=data
}


int main(){
	
	head = (struct node *)malloc(sizeof(struct node));

	int data,ch,n,i;
	printf("Enter the size of list" );
	scanf("%d",&n);

	for(i=0;i<n;i++){
		scanf("%d",&data);
		insert(data);
	}

	struct node *temp=head;
	while (temp->next!=	NULL){
		printf("->%d",temp->data);
		temp=temp->next;
	}
	return 0;
}