package BinaryTree;

class Node{
    int data;
    Node left,right;
    public Node (int value){
        this.data = value;
        this.left=this.right =null;
    }
}

public class BinaryTree {

//    protected BinaryTree(){
//        Node head = null;
//    }
    protected Node insert(int data, Node head){

        if(head == null){
            return  new Node(data);
        }

        if(data < head.data){
            head.left = insert(data, head.left);
        }
        else if(data> head.data){
            head.right= insert(data,head.right);
        }

        return head;
    }

    protected Node Min(Node root){
        if(root==null){
            return null;
        }
        Node temp = root;
        while(temp.left!=null){
            temp = temp.left;
        }
        return temp;
    }

    protected Node remove(int data, Node root){
        if(root == null){
            return null;
        }
        if(data < root.data){
            root.left = remove(data,root.left);
        }
        else if(data > root.data){
            root.right = remove(data, root.right);
        }
        else{
            if(root.left == null){
                return root.right;
            }
            else if (root.right == null){
                return root.left;
            }
            else{
                Node min = Min(root.right);
                root.data = min.data;
                root.right = remove(min.data,min);
            }
        }
        return root;
    }
}
