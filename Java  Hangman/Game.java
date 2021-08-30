import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class Game implements ActionListener{
   
   private JTextField txfGuess;
   private String rWord;
   private JTextArea txfOutput;
   private String[] guessed;
   private String g = "";
   private int image = 1;
   private JButton button;
   private boolean isWrong = true;
   
   public Game(JTextField txfGuess, String rWord, JTextArea txfOutput, String[] guessed, JButton button){
   
      this.txfGuess = txfGuess;
      this.rWord = rWord;
      this.txfOutput = txfOutput;
      this.guessed = guessed;
      this.button = button;
   }
   // controls the difficulty of the game according to the user input
   public int getLevel(int difficulty){
      
      if(difficulty == -1)
         image = 0; 
      image+= difficulty;
      return image;
   }
   public boolean getWrong(){
      
      return isWrong;}
   
   /* Action perfomed when the guess button is clicked.
   Checks whether the letter guessed by the user is part of the random word
   and adds to an array which will be used for displaying output. gives user feedback for their guess
   */
   public void actionPerformed(ActionEvent e){
      try{
         g = "";
         String letter = txfGuess.getText();
         txfOutput.append("Guess \'" + letter + "\'\n");
      
         isWrong = true;
      
         int index =0;
         while(rWord.indexOf(letter,index)!=-1){ // checks for matching letters
         
         // matching letter is added to the array accoring to its postion on the word
            guessed[rWord.indexOf(letter,index)]=letter;
            index = rWord.indexOf(letter,index)+1;
            isWrong = false;
         
         }
      
      
         
         for (String guess : guessed){
            g += guess;
         }
         if (isWrong == true) {
            txfOutput.append("Wrong\n"); // gives feedback for a wrong guess
         } 
         else if(g.equals(rWord)){
            txfOutput.append(g);
            txfOutput.append("\n************************\nYou Win!!!");// gives feedback if the user guessed all the letters of the random word
            txfGuess.setEditable(false);
            button.setEnabled(false);
         
         }
         else{
            txfOutput.append(g + "\n");
         }
         
      }
      catch(Exception er){
         System.out.println(er.toString());
      }
      
      
   }
   
}