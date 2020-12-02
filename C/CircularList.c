#include<stdio.h>
#include<stdlib.h>


//curcular linklist
struct node
{
	int data;
	struct node *next;
	
};
//maintain the last pointer ->data->data(last)->

struct node *last;

void delete(int data){
	//first //last// end;
	if(last==NULL){
		printf("List Empty");
		return;
	}


	struct node * curr=last->next;
	struct node * prev=NULL;

	while(curr->data!=data && curr != last){
		prev=curr;
		curr=curr->next;
	}
	//last
	if(curr==last){
		prev->next=curr->next;
		last=prev;
		free(curr);
		return;
	}
	//first

	if(prev==NULL){
		last->next=curr->next;
		free(curr);
		return;
	}

	if(curr !=last && prev!=NULL){
		prev->next=curr->next;
		free(curr);
		return;

	}

}

void insert_end(int data){
	struct node * newNode=(struct node*)malloc(sizeof(struct node));
	newNode->data=data;
	if(last==NULL){
		last=newNode;
		newNode->next=last;
		return;
	}

	newNode->next=last->next;
	last->next=newNode;
	last=newNode;
}

void insert_beg(int data){
		struct node * newNode=(struct node*)malloc(sizeof(struct node));
	
	newNode->data=data;
	if(last==NULL){
		last=newNode;
		newNode->next=last;
		return;
	}
		newNode->next=last->next;
		last->next=newNode;

}

void printList(){
	if(last==NULL){
		return;
	}
	struct node * temp= last->next;
	do{
		printf("->%d",temp->data );
		temp=temp->next;
	}
	while(temp!=last->next);
}

int main(){
	int data, n,i;
	printf("Enter the number of nodes");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&data);
		insert_end(data);


	}

printList();
printf("\n");
	delete(5);

printList();
return 0; 

}