package BinaryTree;
public class BTProperties extends BinaryTree {
    private void Inorder(Node head){
        if(head==null){
            return;
        }
        Inorder(head.left);
        System.out.println(head.data);
        Inorder(head.right);

    }
    private void Preorder(Node head){
        if(head==null){
            return;
        }
        System.out.println(head.data);
        Preorder(head.left);
        Preorder(head.right);

    }
    private void Postorder(Node head){
        if(head==null){
            return;
        }
        Postorder(head.left);
        Postorder(head.right);
        System.out.println(head.data);

    }

    private void PrintUtil(int arr [], int n){
        for(int i=0;i<=n;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    private void Nodes_with_right_child_only(Node head){
        if(head==null){
            return;
        }
        if(head.right!=null){
            System.out.println(head.data);
        }
        Nodes_with_right_child_only(head.left);
        Nodes_with_right_child_only(head.right);

    }
    private int Sum_of_all_nodes(Node head){
        if(head==null){
            return 0;
        }
        return head.data+Sum_of_all_nodes(head.left)+Sum_of_all_nodes(head.right);
    }

    private int update_nodes_with_sum(Node head){
        if(head==null){
            return 0;
        }
        head.data += update_nodes_with_sum(head.left)+update_nodes_with_sum(head.right);
        return head.data;
    }

    private boolean Search(Node head, int data){
        if(head == null){
            return false;
        }
        if(head.data == data){
            return true;
        }
        return (Search(head.left, data) || Search(head.right, data));
    }

    private boolean PrintAncestors(Node head, int data){
        if(head==null){
            return false;
        }
        if(head.data == data){
            System.out.print(head.data+" ");
            return true;
        }
        boolean a = PrintAncestors(head.left,data);
        boolean b = PrintAncestors(head.right,data);
        if (a||b){
            System.out.print(head.data+" ");
        }
        return a||b;
    }

    private void LeafPathUtil(Node head, int [] arr, int idx){
        if(head==null){
            return;
        }
        arr[idx] = head.data;
        if(head.left==null && head.right==null){
            PrintUtil(arr,idx);
            return;
        }
        LeafPathUtil(head.left, arr,idx+1);
        LeafPathUtil(head.right,arr,idx+1);
    }

    private void LeafPaths(Node head, int n){
        int arr [] = new int [n+1];
//        PrintUtil(arr,n);
        LeafPathUtil(head,arr,0);
    }

    public static void main(String [] args){
        Node head = null;
        BTProperties BT = new BTProperties();
        head = BT.insert(5,head);
        head = BT.insert(3,head);
        head = BT.insert(4,head);
        head = BT.insert(10,head);
        head = BT.insert(20,head);
        head = BT.insert(8,head);
        head = BT.insert(9,head);
//        BT.Preorder(head);
//        System.out.println(BT.update_nodes_with_sum(head));
//        BT.Preorder(head);
//        System.out.println(BT.Search(head,5));
//        BT.LeafPaths(head,7);
//        BT.PrintAncestors(head,20);
    }

}
