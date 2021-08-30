import java.io.*; 
import java.util.Scanner;

public class Generate{

   public static void main(String args[]){
      
      int i=0;
      String subSet[] = new String[20];
      String date;
   
      try{
      
         Scanner sc = new Scanner(new File("cleaned_data.csv"));    
         sc.nextLine();
         while (i<20){
         
            String lines[] = sc.nextLine().split(",");
            subSet[i] = lines[0];
            i++;
         }
      
         sc.close();
         i=0;
         PowerBSTApp tree = new PowerBSTApp();
         PowerArrayApp paa= new PowerArrayApp();
         tree.insertV();
         paa.printAllDateTimes();
         while(i<20){
               
            tree.search(tree.root,subSet[i]);
            paa.printDateTime(subSet[i]);
            i++;
         } 
      }
      catch(Exception e){}
   }
}