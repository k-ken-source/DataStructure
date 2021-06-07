package DynamicProgramming;

public class EditDistance {
    // recursive Backward

    public int minEditDistance(String s1, String s2, int i, int j){
        if(i==0) return j;
        if(j==0) return i;

        if(s1.charAt(i-1) == s2.charAt(j-1)){
            return minEditDistance(s1,s2,i-1,j-1);
        }
        int x = minEditDistance(s1,s2,i,j-1);
        int y = minEditDistance(s1,s2,i-1,j);
        int z = minEditDistance(s1,s2,i-1,j-1);
        return 1+ Math.min(x,Math.min(y,z));

    }

    public int minEditDistance(String s1, String s2){
        int m = s1.length();
        int n = s2.length();
        int [][] dp = new int [m+1][n+1];

        for(int i=0;i<=m;i++){
            for(int j=0;j<=n;j++){
                if(i==0){
                    dp[i][j] = j;
                }
                if(j==0){
                    dp[i][j] = i;
                }
            }
        }

        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if( s1.charAt(i-1) == s2.charAt(j-1) ){
                    dp[i][j] = dp[i-1][j-1];
                }
                else{
                    dp[i][j] = 1+Math.min(dp[i-1][j],Math.min(dp[i][j-1],dp[i-1][j-1]));
                }
            }

        }
        return dp[m][n];
    }

    public static void main(String args []){
        EditDistance obj = new EditDistance();
        String s1 = "intention";
        String s2 = "execution";

         int result = obj.minEditDistance("intention","execution");
         System.out.println(result);
    }
}
//"intention"
//        "execution"
