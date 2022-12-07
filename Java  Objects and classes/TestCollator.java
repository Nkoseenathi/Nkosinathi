public class TestCollator{

   private TestCollator() {}

   public static void main(final String[] args) {
     //Test 1   
      System.out.println("Test 1");
      Collator col = new Collator("Default");
      col.label("Nkosi");
   
      if(col.label().equals("Nkosi")){
         System.out.println("Pass"); 
      }
      
      else{
         System.out.println("Fail");
      }
    
      int test[]={1,2,3,4,5};
      for(int i=0;i<5;i++){
      
         col.recordReading(test[i]);
      }
   //Test 2
      col = new Collator("Default");
      col.label("Nkosi");
      System.out.println("Test 2");
   
      if(col.maximum()==5){
      
         System.out.println("Pass");
      }
      
      else{
         System.out.println("Fail");      
      }
   
   //Test 3
      col = new Collator("Default");
      col.label("Nkosi");
      System.out.println("Test 3");
   
      if(col.minimum()==1){
         System.out.println("Pass");
      }
      
      else{
         System.out.println("Fail");
      }
   
   //Test 4
      col = new Collator("Default");
      col.label("Nkosi");
      System.out.println("Test 4");
   
      try{
         if(col.average()==3.0){
         
            System.out.println("Pass");
         }
         else{
            System.out.println("Fail");
         }
      }
      catch(Exception e){
      }
   
   //Test 5
      col = new Collator("Default");
      col.label("Nkosi");
      System.out.println("Test 5");
   
      if(col.numberOfReadings()==5){
      
         System.out.println("Pass");
      }
      
      else{
         System.out.println("Fail");
      }
   } 
}   
    
    
    
    
    
    
    
    
    
    
    
    
   










