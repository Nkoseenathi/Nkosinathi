import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PatternMatcher implements ActionListener{
   
   private JTextField txfInput;
   private JTextArea txaOutput;
   private WordList wordlist;
   
   public PatternMatcher(JTextField txfInput, WordList wordlist, JTextArea txaOutput){
   
      super();
      this.txfInput = txfInput;
      this.wordlist = wordlist;
      this.txaOutput = txaOutput;
   }



   public void actionPerformed(ActionEvent e){
   
      /* Acion perfomed when the user clicks the search button
         retrieves words from the dictionary text document
         and checks whether any of the words has the same pattern 
         as the one entered by the user, if they do they are displayed
         on text area*/
         
      Pattern pattern = new Pattern(txfInput.getText());
      
      try{
      
         wordlist = WordList.readFromFile("dictionary.txt");//get the words from the dictionary text file
      }
      catch(Exception ex){
      
         System.out.println(ex.toString());
      }
            
      for(Word word:wordlist){
      
         if(pattern.matches(word))
         
            txaOutput.append(word+"\n");//display words that match user input
         
      }
      
      txfInput.setText(null);
   }
}