package DynamicProgramming;

import java.util.Scanner;

//Find the number of ways to reach the Nth stair, we can move only 1 step and 2 step;
// Also the minimum number of steps
public class WaysToReachNthStrair {

    public int minways(int n){
        if(n==1 || n==2){
            return 1;
        }
        int x = minways(n-1);
        int y = minways(n-2);
        return Math.min(x,y)+1;
    }

    public int ways(int n){
        int a = 1;
        int b = 1;
        int temp;
        for(int i=2;i<=n;i++){
            temp = a+b;
            a = b;
            b = temp;
        }
        return b;
    }
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        WaysToReachNthStrair obj = new WaysToReachNthStrair();
        long res = obj.ways(n);
        System.out.println(res);
    }
}
