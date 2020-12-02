#include<stdio.h>
#include<stdlib.h>
#define COUNT 10

struct node{
	int data;
	int h;
	struct node * left;
	struct  node * right;
};

struct node * head;

int max(int a, int b){
	return (a>=b)? a:b;
}

int height(struct node * node){
	if (node==NULL){
		return -1;
	}
	return node->h;
}

struct node * min(struct node * root){

	struct node * temp = root; 
	while(temp->left!=NULL){
		temp=(temp->left);
	}
		return temp;
}

struct node * newNode(int data){
	struct node * node= (struct node *)malloc(sizeof(struct node));
	node->data=data;
	node->h=0;
	node->left=NULL;
	node ->right =NULL;
	return node;

}

struct node * RightRotation(struct node * root){
	struct node * x=root->left;
	root->left=x->right;
	x->right=root;

	root->h = max(height(root->right),height(root->left))+1;

	x->h = max(height(x->right),height(x->left))+1;

	return x;
}

struct node * LeftRotation(struct node * root){
	struct node * x=root->right;
	root->right=x->left;
	x->left=root;

	root->h = max(height(root->right),height(root->left))+1;

	x->h = max(height(x->right),height(x->left))+1;

	return x;

	return x;
}

int Balance(struct node * node){

	return abs(height(node->left)-height(node->right));
}

struct node * insert(struct node * head, int data){
	

	if(head==NULL){
		return newNode(data);
	}

	if (head->data > data){
		head->left = insert(head->left, data);
	}

	else{
		head->right = insert(head->right,data);
	}

	head->h=1+max(height(head->right),height(head->left));

	if(Balance(head)>1 && data>head->data){
		struct node * temp=head->right;
		if(data>temp->data){
			head=LeftRotation(head);
		}
		else{
			head->right=RightRotation(temp);
			head=LeftRotation(head);
		}
	}

	if(Balance(head)>1 && data<head->data){
		struct node * temp=head->left;
		if(data<temp->data){
			head=RightRotation(head);
		}

		else{
			head->left=LeftRotation(temp);
			head=RightRotation(head);
		}
	}
	return head;

}

struct node * delete(struct node * root, int data){
	if(root==NULL){
		return NULL;
	}

	if(root->data > data){
		root->left=delete(root->left,data);
	}

	else if(root->data < data){
		root->right = delete(root->right,data);
	}

	else{

		if(root->right==NULL){
			struct node * temp=root->left;
			free(root);
			return temp;
		}

		else if(root->left == NULL){
			struct node * temp=root->right;
			free(root);
			return temp;
		}
		else{
			struct node * temp=min(root->right);
			root->data=temp->data;
			root->right=delete(root->right,temp->data);
		}

	}

	root->h=1+max(height(root->right),height(root->left));

	if(height(root->right) >= 2+height(root->left)){
		if(height(root->right->right)>height(root->right->left)){
			root=LeftRotation(root);
		}

		else{
			root->right=RightRotation(root->right);
			root=LeftRotation(root);
		}
	}

	else if(height(root->left) >= 2+height(root->right)){
		if(height(root->left->left)>height(root->left->right)){
			root=RightRotation(root);
		}

		else{
			root->left=LeftRotation(root->left);
			root=RightRotation(root);
		}
	}

	return root; 
}

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

void inorder(struct node *root) 
{ 
    if (root != NULL) 
    { 
        inorder(root->left); 
        printf("->%d", root->data); 
        inorder(root->right); 
    } 
} 

int main(){
	int n,i,d;

	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&d);
		head=insert(head,d);
	}

	print2D(head);
	inorder(head);
	
	printf("\n Minimum value");
	struct node * minval=min(head);
	printf("%d",minval->data);
	
	printf("\n After deletion and Insertion");
	delete(head,4);
	head= insert(head,-100);
	head= insert(head,-10);
	head = delete(head,10);
	
	print2D(head);
	inorder(head);
}