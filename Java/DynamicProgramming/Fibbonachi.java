package DynamicProgramming;

import java.util.Scanner;

public class Fibbonachi {
    public int Fibbo(int n){
        int a = 0;
        int b = 1;
        int result = 0;
        for(int i=2;i<=n;i++){
            result = a+b;
            a = b;
            b = result;
        }
        return result;
    }

    public static void main(String args []){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Fibbonachi obj = new Fibbonachi();
        long res = obj.Fibbo(n);
        System.out.println(res);
    }
}
