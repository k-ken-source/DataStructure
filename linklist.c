#include<stdio.h>
#include<stdlib.h>
//pop
//push
//insert_at()

struct node{
	int data;
	struct node* next;
};

struct node *head=NULL;

void printList(){
	struct node *temp=head;
	while(temp!=NULL){
		printf("->%d",temp->data );
		temp=temp->next;

	}
}

void delete(int data){
	struct node * curr=head;
	struct node * prev=NULL;

	while(curr!=NULL && curr->data!=data){
		prev=curr;
		curr=curr->next;
	}
	if(curr==NULL){
		return;
	}

	//first element

	if(prev==NULL){
		if(curr->next==NULL){
			head=NULL;
		}
		else{
			head=head->next;
		}
	free(curr);
	return;
	}

	//last element;
	if (curr->next==NULL){
		prev->next=NULL;

		free(curr);
		return;
	}
	//middle element;
	if(curr->next!=NULL && prev!=NULL){
		prev->next = curr->next;
		free(curr);
		return;

	}

}

void pop(){
	struct node * curr=head;
	struct node * prev=NULL;

	while(curr->next!=NULL){
		prev=curr;
		curr=curr->next;
	}
	prev->next=NULL;
	free(curr);

}

void insert(int data, int index){
	int idx=0;
	struct node * newNode=(struct node *)malloc(sizeof(struct node));
	struct node * curr=head;
	struct node * prev=NULL;

	newNode->data = data;
	if(head==NULL){
		newNode->next=NULL;
		head=newNode;
		return;
	}

	//at begining;
	if(index==0){
		newNode->next = head;
		head=newNode;
		return;
	}
	//at the end;
	while(curr!=NULL && idx!=index){
		prev=curr;
		curr=curr->next;
		idx+=1;
	}
	if(curr==NULL){
		prev->next=newNode;
		newNode->next=NULL;
		return;
	}
	//middle;

	prev->next=newNode;
	newNode->next=curr;

}

void append(int data){
	insert(data,-1);
}
int main(){

	int n,i,data;
	printf("Enter the number of nodes");
	scanf("%d",&n);

	for(i=0;i<n;i++){
		scanf("%d",&data);
		append(data);
	}
	printList();

	//insert(23,6);
	printf("\n");
	printList();
	//pop();
	delete(5);
	printf("\n");
	printList();

	return 0;
}