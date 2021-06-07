import java.util.Scanner;

public class GlassProblem {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        double cap = sc.nextInt();
        double waterL = sc.nextInt();
        PrintGlassPattern Obj = new PrintGlassPattern();
        Obj.PrintCreateArray(cap,waterL);

    }

    private static class PrintGlassPattern{
//        int cap,water;
//        public PrintGlassPattern(int cap, int water){
//            this.cap = cap;
//            this.water = water;
//            //PrintCreateArray(cap,water);
//        }

        private void PrintCreateArray(double cap, double water){

            double arr[][] = new double [100][100];
            boolean overflow = true;
            arr[0][0] = water;
            int row = 0;
            while(overflow){
                overflow = false;
                for(int col=0;col<=row;col++){
                    if(arr[row][col]>cap) {
                        overflow = true;
                        double temp = (arr[row][col] - cap);
                        arr[row + 1][col] += temp / 2;
                        arr[row + 1][col + 1] += temp / 2;
                        arr[row][col] = cap;
                    }
                }
                row++;
            }


            for(int i=0;i<row;i++){
                for(int j=0;j<=i;j++){
                    System.out.print(arr[i][j]+" ");
                }
                System.out.println();
            }
        }
    }
}
