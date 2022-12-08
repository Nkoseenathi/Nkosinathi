import java.util.*;
import java.io.*;

public class Sequential{

   static long startTime = 0;
	
   private static void tick(){
      startTime = System.currentTimeMillis();
   }
   private static float tock(){
      return (System.currentTimeMillis() - startTime) / 1000.0f; 
   }

   public static void main(String args[]){
   
      try{
         String fn = args[0];
         Scanner sc = new Scanner(new File(fn+".txt"));
         String dim = sc.nextLine();
         int row =Integer.parseInt(dim.split(" ")[0]);
         int col =Integer.parseInt(dim.split(" ")[1]);
         float a[][]=new float[row][col];
         boolean basin = true;
         int baseen =0;
         ArrayList<String> bList = new ArrayList<String>();
      
         while(sc.hasNextFloat()){     
            	
             for(int i = 0;i<row;i++){
               for(int j = 0;j<col;j++){
                  a[i][j] = sc.nextFloat();}
            }
         }
      
      
         System.gc();
         tick();
         for(int i=1; i < row-1; i++){
         
            for(int j = 1;j<col-1;j++){
            
               if((a[i-1][j]-a[i][j])<0.01){
                  basin = false;
               }
            
               if((-a[i][j]+a[i][j-1])<0.01){  
                  basin = false;
               }
            
               if((-a[i][j]+a[i+1][j])<0.01){
                  basin = false;
                     
               }
                  
               if((-a[i][j]+a[i][j+1])<0.01){
                  basin = false;
               }
                  
               if((-a[i][j]+a[i+1][j-1])<0.01){
                  basin = false;
               }
            
               if((-a[i][j]+a[i-1][j-1])<0.01){
                  basin = false;
               }
            
               if((-a[i][j]+a[i-1][j+1])<0.01){
                  basin = false;
               }
            
               if((-a[i][j]+a[i+1][j+1])<0.01){
                  basin = false;
               }
            
               if(basin == true){
                  baseen++;
                  bList.add(i+" "+j);
               }
               basin =true; 
            }
         }
         
         float time = tock();
         			 
         FileWriter fileWriter = new FileWriter(args[1]+".txt");
         PrintWriter pw = new PrintWriter(fileWriter);
         
         int len = bList.size();
         pw.println(len);      
         for(int x =0; x<len;x++){
            pw.println(bList.get(x));
         }
         pw.close();
      }
      
      catch(Exception e){
      
         e.printStackTrace();      
      }
   }
}

   
    






















