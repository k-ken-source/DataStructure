#include<stdio.h>
#include<stdlib.h>
#define COUNT 10 
struct node
{
	int data;
	struct node * left;
	struct node * right;
};



void print2DUtil(struct node *root, int space) 
{ 
    // Base case 
    if (root == NULL) 
        return; 
  
    space += COUNT; 
  
    print2DUtil(root->right, space); 
  
    printf("\n"); 
    for (int i = COUNT; i < space; i++) 
        printf(" "); 
    printf("%d\n", root->data); 
  
    print2DUtil(root->left, space); 
} 
  

void print2D(struct node *root) 
{ 

   print2DUtil(root, 0); 
}

struct node * Search(struct node * root,int data){
	struct node * temp=NULL;
	if(root==NULL){
		printf("Not Found");
		return NULL;
	}
	if(root->data==data){
		return root;
	}
	if(root->data>data){
		temp=Search(root->left,data);
	}
	else{
		temp=Search(root->right,data);
	}
	return temp;
}

void inorder(struct node *root) 
{ 
    if (root != NULL) 
    { 
        inorder(root->left); 
        printf("->%d", root->data); 
        inorder(root->right); 
    } 
} 

void max(struct node * root){
	struct node * temp=root;

	if(temp->right!=NULL){
		max(temp->right);
	}
	else{
		printf("Max Value: %d\n",temp->data);
		return;
	}

	}

struct node * min(struct node * root){
	struct node * temp=root;

	if(temp->left!=NULL){
		min(temp->left);
	}
	else{
			return temp;
	}
	}

struct node * newNode(int data){
	struct node * temp=(struct node *)malloc(sizeof(struct node));
	temp->data=data;
	temp->left=NULL;
	temp->right=NULL;
}

struct node * insert(struct node * root, int data){
	
	if(root==NULL){
		return newNode(data);
	}
	if(root->data > data){
		root->left=insert(root->left,data);
	}
	else{
		root->right=insert(root->right,data);
	}
	return root;
}

struct node * Next_Largest(struct node * root, struct node * n){
	struct node * temp=NULL;

	if (n->right!=NULL){
		return min(n->right);
	}
	while(root!=NULL){
		if(n->data < root->data){
			temp=root;
			root=root->left;
		}
		else if(n->data > root->data){
			temp=root;
			root=root->right;
		}
		else{
			break;
		}
	}
	return temp;
}

struct node * delete(struct node * root, int value){

	if(root==NULL){
		return NULL;
	}
	if(root->data > value){
		root->left=delete(root->left,value);
	}

	else if(root->data < value){
		root->right=delete(root->right,value);
	}
	else{
		if(root->left==NULL){
			struct node * temp=root->right;
			free(root);
			return temp;
		}

		else if(root->right==NULL){
			struct node * temp=root->left;
			free(root);
			return temp;
		}
		else{

		struct node * temp=min(root->right);
		root->data=temp->data;
		root->right=delete(root->right,temp->data);
		}
		
	}
	return root;
}

int main(){
	struct node * root=NULL;
	struct node * temp=NULL;

	int data,n,i;
	printf("Enter the number of nodes to inserted");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&data);
		root=insert(root,data);
	}
	inorder(root);
	printf("\n");
	max(root);

	temp=min(root);
	printf("Min : %d\n",temp->data);
	//temp=Next_Largest(root,Search(root,56));
	//printf("Next Largest : %d\n",temp->data);
	delete(root,56);

	print2D(root);
	inorder(root);
	return 0;
}