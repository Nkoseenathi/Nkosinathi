import java.io.*; 
import java.util.Scanner;
 
 
public class PowerArrayApp{
 
   public PowerArrayApp(){}
 
   Scanner sc;
   private String time[] = new String[500];
   private int i=0;
   private int opCount=0;
      
    /*Opens the csv file for reading*/ 
   public void open(){
         
      try{
      
         sc = new Scanner(new File("cleaned_data.csv"));
      
      }catch(Exception e){}
   }
       
   /* This method is used to add all the lines in the csv file and returns a string array of all of them
   */          
   public String[] printAllDateTimes(){
      i=0;
      open();
      sc.nextLine();
      while (sc.hasNextLine()){
         
         time[i] = sc.nextLine();
         i++;
      }
   
      sc.close(); 
      return time;
   
   }
   
       
   /* Searches a dateTime value and return the dateTime, global active power and voltge values
   *  @param dateTime the dateTime that is going to be search
   */  
   public String printDateTime(String dateTime){
      open();
      opCount=0;
      boolean check = false;
      time = sc.nextLine().split(",");
      i=0;
   
      while((!(time[0].equals(dateTime))&&i<500)&&sc.hasNextLine())
      {     
         time = sc.nextLine().split(",");
         opCount++;
         if(time[0].equals(dateTime)){
         
            check = true;
            break;
         }
      
      }
      
      sc.close();
      writeToFile();
   
      if (check == true)
         return (time[0]+"\t"+"\t"+time[1]+"\t"+time[3]);
            
      else
         return  "Date/time not found";   
      
   }
   /* Writes the operational counter to a text file
      @param e fileNotFoundException if the to be written to is not found 
   */
   public void writeToFile(){
     
      try{
      
         if(!(new File("InstrumentationAr.txt")).exists()){
            PrintWriter pw = new PrintWriter(new FileWriter(new File("InstrumentationAr.txt")));
            pw.println(opCount);
            pw.close();}
         
         else{
            PrintWriter pw = new PrintWriter(new FileWriter(new File("InstrumentationAr.txt"),true));
            pw.println(opCount);
            pw.close();
         }
      
      }
      catch(Exception e){
      
         System.out.println(e.toString());
       
      } 
   }
          
      
}
