//doubly link list 
#include<stdio.h>
#include<stdlib.h>

struct node{
	int data;
	struct node * next;
	struct node * prev;

};
struct node * head;

void printList(){
	struct node * temp = head;
	while(temp!=NULL){
		printf("->%d",temp->data);
		temp=temp->next;
	}
}

void delete(int data){
	struct node * temp=head;
	struct node * prev=NULL;
	while(temp->data!=data && temp!=NULL){
		temp=temp->next;
	}
	if(temp==head){

	head=head->next;
	head->prev=NULL;
	free(temp);
	return;
	}

	prev=temp->prev;
	prev->next=temp->next;
	free(temp);

}

void insert(int data,int index){
	struct node * newNode = (struct node *)malloc(sizeof(struct node));
	if(head==NULL){
		newNode->next=NULL;
		newNode->prev=NULL;
		head=newNode;
		return;
	}

	
	int idx=0;
	struct node * temp=head;
	struct node * p=NULL;

	newNode->data=data;

	while(temp!=NULL && idx !=index){
		p=temp;
		temp=temp->next;
		idx+=1;
	}

	//first element
	if(idx=0){
		temp->prev=newNode;
		newNode->next=temp;
		head=newNode;
		return;
	}
	//last element
	if(temp==NULL){
		newNode->next=NULL;
		newNode->prev=p;
		p->next=newNode;
		return;
	}

	//middle element;
		p=temp->prev;
		p->next=newNode;
		newNode->prev=p;
		newNode->next=temp;
		temp->prev=newNode;
		return;


}


void insert_beg(int data){

	struct node * newNode=(struct node *)malloc(sizeof(struct node));
	newNode->data=data;
	if(head==NULL){

		newNode->next=NULL;
		newNode->prev=NULL;
		head=newNode;
		return;

	}
	head->prev=newNode;
	newNode->next=head;
	newNode->prev=NULL;
	head=newNode;


}

void insert_end(int data){
	struct node * newNode=(struct node *)malloc(sizeof(struct node));
	struct node * temp=head;
	newNode->data = data;

	if(head==NULL){
		newNode->next=NULL;
		newNode->prev=NULL;
		head=newNode;
		return;
	}
	while(temp->next!=NULL){
		temp=temp->next;
	}


	newNode->next=NULL;
	newNode->prev=temp;
	temp->next=newNode;
}

int main()
{

	int n, data,i;
	printf("Enter the number the of nodes" );
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&data);
		insert_end(data);
	}

	printList();
	printf("\n");

	delete(1);


	printList();

	return 0;
}