import java.util.Scanner;
public class  Meteorology{

   private  Meteorology(){}

   public static void main(final String[] args) {
      int sel = 0;
      int val = 0;
      String tm="";
      String pr="";
      String hm="";
      Collator temp = new Collator("temperature");
      Collator pre = new Collator("pressure");
      Collator hum = new Collator("humidity");
      
      Scanner sc = new Scanner(System.in);
      System.out.println("Meteorology Program");
   
      do{
         
         System.out.println("Make a selection and press return:");
         System.out.println("1. Record a temperature reading.");
         System.out.println("2. Record a pressure reading.");
         System.out.println("3. Record a humidity reading.");
         System.out.println("4. Print maximum values.");
         System.out.println("5. Print minimum values.");
         System.out.println("6. Print average values.");
         System.out.println("7. Quit.");
      
         sel = sc.nextInt();
         String err = sc.nextLine();
         
         
         if(sel == 7) 
            break;
         
         if (sel<4){
            System.out.println("Enter value:");
            val= sc.nextInt();
         }
         switch(sel){
         
            case 1:
               
               temp.recordReading(val);
               break;
               
            case 2:
               pre.recordReading(val);
               break;
             
            case 3:
               hum.recordReading(val);
               break;
             
            case 4:
            
               if(temp.maximum()==0)
                  System.out.println("Maximum temperature: -");
               else
                  System.out.println("Maximum temperature: "+temp.maximum());
               if(pre.maximum()==0)
                  System.out.println("Maximum pressure: -");
               else
               
                  System.out.println("Maximum pressure: "+pre.maximum());
               if(hum.maximum()==0)
                  System.out.println("Maximum humidity: -");
               else
                  System.out.println("Maximum humidity: "+hum.maximum());
               break;
           
            case 5:
               if(temp.minimum() == 0)
                  System.out.println("Minimum temperature: -");
               else
                  System.out.println("Minimum temperature: "+temp.minimum());
               if(pre.minimum() == 0)
                  System.out.println("Minimum pressure: -");
               else
                  System.out.println("Minimum pressure: "+pre.minimum());
               if(hum.minimum() == 0)
                  System.out.println("Minimum humidity: -");
               else
                  System.out.println("Minimum humidity: "+hum.minimum()); 
               break;
               
            case 6:
               String test = temp.average()+"";
               if (temp.average()==0||test.equals("NaN")){
               
                  tm= "-";
                  System.out.println("Average temperature: "+tm);
                  
               }
               else{
               
                  tm = temp.average()+"";
                  System.out.printf("Average temperature: %.2f",Double.parseDouble(tm));
                  System.out.println();}
                 
               test = pre.average()+"";
               if(pre.average()==0||test.equals("NaN")){
               
                  pr="-";
                  System.out.println("Average pressure: "+pr);
                  
               }
               else{
               
                  pr = pre.average()+"";
                  System.out.printf("Average pressure: %.2f",Double.parseDouble(pr));
                  System.out.println();}
               
               test = hum.average()+"";
               if(hum.average()==0||test.equals("NaN")){
               
                  hm="-";
                  System.out.println("Average humidity: "+hm);
                  
               }
               else{
                  hm = hum.average()+"";
                  System.out.printf("Average humidity: %.2f",Double.parseDouble(hm));}
               System.out.println();
               break;
         }
      }
      while(sel!=7); 
   }
}