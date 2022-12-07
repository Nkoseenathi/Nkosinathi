import java.io.*; 
import java.util.Scanner;

class PowerBSTApp { 
 
   /* Class containing left and right child of current node and key value*/
   int opCount=0;

   class Node { 
      String key; 
      Node left, right; 
   
      public Node(String item) { 
         key = item; 
         left = right = null; 
      } 
   } 
 
   // Root of BST 
   Node root; 
 
   // Constructor 
   PowerBSTApp() {  
      root = null;  
   } 
      // This method mainly calls insertRec() 
   void insert(String key) { 
      root = insertRec(root, key); 
   } 
     
   /* A recursive function to insert a new key in BST */
   Node insertRec(Node root, String key) { 
   
      /* If the tree is empty, return a new node */
      if (root == null) { 
         root = new Node(key); 
         return root; 
      } 
   
      /* Otherwise, recur down the tree */
      if (key.split(",")[0].compareToIgnoreCase(root.key.split(",")[0])>0) 
         root.left = insertRec(root.left, key); 
      
      else if (key.compareToIgnoreCase(root.key)<0) 
         root.right = insertRec(root.right, key); 
   
      /* return the (unchanged) node pointer */
      return root; 
   } 
      // This method mainly calls InorderRec() 
   void inorder()  { 
      inorderRec(root); 
   } 
 
   // A utility function to do inorder traversal of BST 
   void inorderRec(Node root) { 
      if (root != null) { 
         inorderRec(root.left); 
         String ary[] = root.key.split(",");
         System.out.println(ary[0]+"\t"+ary[1]+"\t"+ary[3]); 
         inorderRec(root.right); 
      } 
   }
    
   public Node search(Node root, String key) 
   { 
    // Base Cases: root is null or key is present at root 
      opCount++;
      if (root==null || root.key.split(",")[0].compareToIgnoreCase(key.split(",")[0])==0){
         writeToFile();
         opCount=0;
         return root; 
      }
   
    // val is greater than root's key 
      if (root.key.split(",")[0].compareToIgnoreCase(key)<0) 
         return search(root.left, key); 
   
    // val is less than root's key 
      return search(root.right, key); 
   }

   public void writeToFile(){
      try{
         if(!(new File("InstrumentationBST.txt")).exists()){
            PrintWriter pw = new PrintWriter(new FileWriter(new File("InstrumentationBST.txt")));
            pw.println(opCount);
            pw.close();}
         
         else{
            PrintWriter pw = new PrintWriter(new FileWriter(new File("InstrumentationBST.txt"),true));
            pw.println(opCount);
            pw.close();}
      
      }
      catch(Exception e){
      
         System.out.println(e.toString());
       
      } 
   }
   public void insertV(){
      try{ 
      
         Scanner sc = new Scanner(new File("cleaned_data.csv"));
         sc.nextLine();
      
         while(sc.hasNextLine()){
            insert(sc.nextLine()); 
         }
         sc.close();
      
        // print inorder traversal of the BST 
         inorder(); 
      }
      catch(Exception e){} 
   }
} 

   
