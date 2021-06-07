package DynamicProgramming;

import java.util.Scanner;

//Program for finding factorial.
public class Factorial {
    public long factorial (int n){
        long dp [] = new long[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i=2;i<=n;i++){
            dp[i] = i*dp[i-1];
        }
        return dp[n];
     }

     public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Factorial obj = new Factorial();
        long res = obj.factorial(n);
        System.out.println(res);
     }
}
