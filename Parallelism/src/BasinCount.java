import java.util.*;
import java.util.concurrent.RecursiveTask;

public class BasinCount extends RecursiveTask<Integer> {

   int lo;    
   int hi;
   static ArrayList<String> bList = new ArrayList<String>() ;//Stotres cordinates
   float a[][];
   static final int SEQUENTIAL_CUTOFF=850;
   int baseen = 0;// number of basins 
	    
   BasinCount(float[][] grid, int l, int h) { 
      lo=l; hi=h; a=grid;
   }

/*
Computes the number of basins and adds them to an array
*/
   protected Integer compute(){ 
  
      boolean basin = true;

      if((hi-lo) < SEQUENTIAL_CUTOFF) {
         int baseen = 0;

         //iterate through the array
         for(int i=lo+1; i < hi-1; i++){
         
            for(int j = 1;j<a[0].length-1;j++){
               
            //Check the bottom neighbour
               if((a[i-1][j]-a[i][j])<0.01){   
                  basin = false;
               }

              // Check the left neighbour
               if((-a[i][j]+a[i][j-1])<0.01){  
                  basin = false;
               }

            // Check the top neighbour
               if((-a[i][j]+a[i+1][j])<0.01){
                  basin = false;     
               }

               // Check the right neighbour
               if((-a[i][j]+a[i][j+1])<0.01){
                  basin = false;
               }

              // Check the top left neighbour  
               if((-a[i][j]+a[i+1][j-1])<0.01){
                  basin = false;
               }

               // Check the bottom left neighbour
               if((-a[i][j]+a[i-1][j-1])<0.01){
                  basin = false;
               }

               // Check the bottom right neighbour           
               if((-a[i][j]+a[i-1][j+1])<0.01){
                  basin = false;
               }

               // Check the top right neighbour
               if((-a[i][j]+a[i+1][j+1])<0.01){
                  basin = false;
               }
               
     	       //check if it is a basin or not and add to list if it's a basin
               if(basin == true){
                  bList.add(i+" "+j);// add coordites to list if they are basins
                  baseen++;// Increment the number of basins      
                           
               }

               basin =true;//reset basin to true
            }      
         } 
         
         return baseen;
	}
      
       		  
      else {
      
         BasinCount left = new BasinCount(a,lo,(hi+lo)/2+1);
         BasinCount right= new BasinCount(a,(hi+lo)/2-1,hi);
         left.fork();
         int rightAns = right.compute();
         int leftAns  = left.join();
         return leftAns + rightAns;     
      }
   }  
}