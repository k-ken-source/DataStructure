package DynamicProgramming;

import java.util.Scanner;

public class ToweOfHanaoi {
    public void toh(int n, String s,String d, String e) {
        if (n == 0) {
            return;
        }
        toh(n-1,s,e,d);
        System.out.println("Move "+n+" From "+s+" To "+d);
        toh(n-1,e,d,s);
    }
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ToweOfHanaoi obj = new ToweOfHanaoi();
        obj.toh(n,"Source","Dest","Extra");
    }
}
