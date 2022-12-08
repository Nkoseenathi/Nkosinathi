import java.io.*; 
import java.util.Scanner;

public class PowerBSTAppTest{

   public static void main(String args[]){
   
   PowerBSTApp tree = new PowerBSTApp();
   tree.insertV();   
   Scanner sc = new Scanner(System.in);
   
      if( tree.search(tree.root,sc.nextLine())==null)
         System.out.println("\nDate/time not found");
       
      else
      {
         String ary[] = tree.root.key.split(",");
         System.out.println("\n"+ary[0]+"\t"+ary[1]+"\t"+ary[3]);      
      }  
   }

}