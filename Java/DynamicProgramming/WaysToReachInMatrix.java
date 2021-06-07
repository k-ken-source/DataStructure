package DynamicProgramming;
import java.util.*;
import java.util.Scanner;

// no of ways to reach the n,m cell in a mxn matrix. Movements allowed (down and right)
class Pair{
    int a;
    int b;
    public Pair(int x, int y){
        this.a = x;
        this.b = y;
    }
}
public class WaysToReachInMatrix {
    public int Recursiveways(int n, int m){
//        if(m==0 && n==0){
//            return 0;
//        }
        if(m==0 || n==0){
            return 1;
        }
        return Recursiveways(m-1,n)+Recursiveways(m,n-1);

    }
    public int DPWays(int n, int m){

        int dp[][] = new int [n][m];
        for(int i=1;i<n;i++){
            dp[i][0] = 1;
        }
        for(int i=1;i<m;i++){
            dp[0][i] = 1;
        }
        for(int i=1;i<n;i++){
            for(int j=1;j<m;j++){
                dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[n-1][m-1];
    }

    public void PrintUtil(Pair [] arr, int n){
        for(int i=0;i<n;i++){
            System.out.print("("+arr[i].a+" "+arr[i].b+")->");
        }
        System.out.println();

    }
    public boolean is_valid(int n,int m, int x, int y){
        if(x<n && y<m){
            return true;
        }
        return false;
    }
    public void PrintUniquePath(int n, int m, int x, int y, Pair [] path, int idx){
        if(x==n-1 && y==m-1){
            path[idx] = new Pair(x,y);
            idx+=1;
            PrintUtil(path, idx);
            idx-=1;
            return;
        }
        Pair p = new Pair(x,y);
        path[idx] = p;
        if(is_valid(n,m,x,y)){
            PrintUniquePath(n,m,x+1,y,path, idx+1);
        }
        if(is_valid(n,m,x,y)){
            PrintUniquePath(n,m,x,y+1,path, idx+1);
        }
        return;

    }


    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m  = sc.nextInt();
        WaysToReachInMatrix obj = new WaysToReachInMatrix();

        Pair path [] = new Pair [n+m];
        obj.PrintUniquePath(n,m,0,0, path,0);
//        int res = obj.DPWays(n,m);
//        System.out.println(res);
    }
}
