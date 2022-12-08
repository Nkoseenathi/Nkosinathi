import java.util.*;
import java.io.*;
import java.util.concurrent.ForkJoinPool;


public class Output{

   int lo;    int hi;
   static ArrayList<String> bList = new ArrayList<String>() ;

   float a[][];

   static long startTime = 0;
	
   private static void tick(){
      startTime = System.currentTimeMillis();
   }
   private static float tock(){
      return (System.currentTimeMillis() - startTime) / 1000.0f; 
   }
   static final ForkJoinPool fjPool = new ForkJoinPool();
   static int base(float[][] arr){
      return fjPool.invoke(new BasinCount(arr,0,arr.length));
   }

   public static void main(String args[]){
   
      try{    
         String fn =args[0];
         Scanner sc = new Scanner(new File(fn+".txt"));
         String dim = sc.nextLine();
         int row =Integer.parseInt(dim.split(" ")[0]);
         int col =Integer.parseInt(dim.split(" ")[1]);
         float grid[][]=new float[row][col];
         ArrayList<String>bList;
         
         // Load data to array
         while(sc.hasNextFloat()){     
       
            for(int i = 0;i<row;i++){
         
               for(int j = 0;j<col;j++){
               
                  grid[i][j] = sc.nextFloat();}
            }
         }
         
         System.gc();
         tick();// Start timer
         int len = base(grid);//Sart the forkjoin
         float time = tock();//Store the amount of time
         
         FileWriter fileWriter = new FileWriter(args[1]+".txt");//Create file
         PrintWriter pw = new PrintWriter(fileWriter);
         pw.println(len);
         bList = BasinCount.bList; // get list from the basin count class

         for(int x =0; x<len;x++){
            pw.println(bList.get(x));//store items in file
         }
         pw.close();
      }
      catch(Exception e){
      
         e.printStackTrace();      
      } 
   
   }


}    
   

      
   


   
   
