import java.io.*; 
import java.util.Scanner;

public class PowerArrayAppTest{

   public static void main(String []args){
      int i =0;
      PowerArrayApp paa= new PowerArrayApp();
      String ary[] = paa.printAllDateTimes();
      
      while(i<500){
         String [] time = ary[i].split(",");
         System.out.println(time[0]+"\t"+"\t"+time[1]+"\t"+time[3]);
         i++;
      }
      Scanner sc = new Scanner(System.in);
      System.out.println("\n\n"+paa.printDateTime(sc.nextLine()));
   
   }
   
}