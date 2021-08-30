import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.border.*;
import java.util.*;

public class Hangman{
   
   private static JFrame gameFrame = new JFrame();
   private static JPanel gamePanel = new JPanel();
   private static JLabel lblDifficulty = new JLabel("Difficulty:");
   private static JLabel lblGuess = new JLabel("Guess:");
   private static JLabel lblPicture = new JLabel();
   private static JTextArea txtAFeedBack = new JTextArea();
   private static JTextField txtUserGuess = new JTextField();
   private static JButton btnGuess = new JButton("Start");
   private static JButton btnQuit = new JButton("Quit");
   private static JButton btnRestart = new JButton("Restart");
   private static JScrollPane scroll = new JScrollPane(txtAFeedBack);
   private static JComboBox cmbDifficulty = new JComboBox();
   private static boolean start = false;
   private static String[] UserGuess;
   private static String[] wordList;
   private static int wordIndex = 0;
   private static Game game;
   
   
    // Displays the pictures on the picutre panel    
   public static void getPicture(int picIndex){
   
      String picture = "state"+picIndex+".GIF";
      ImageIcon icon = new ImageIcon(picture);
      lblPicture.setIcon(icon);
   }
   
   public static void GUI(){
      
      lblGuess.setBounds(30,30,50,20);
      txtUserGuess.setBounds(80,30,100,20);
      txtAFeedBack.setEditable(false);
      scroll.setBounds(30,80,150,250);
      lblDifficulty.setBounds(210,30,80,20);
      cmbDifficulty.setBounds(290,30,90,20);
      btnGuess.setBounds(30,370,80,25);
      btnRestart.setBounds(150,370,80,25);
      btnQuit.setBounds(250,370,80,25);
      
      lblPicture.setBounds(210,80,180,250);
      lblPicture.setBorder(BorderFactory.createLineBorder(Color.black));
      
      gamePanel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createLineBorder(Color.black), "Hang man game"));
      gamePanel.setBounds(20, 20, 430, 410);
      gamePanel.setLayout(null);
      gamePanel.add(lblGuess);
      gamePanel.add(txtUserGuess);
      gamePanel.add(cmbDifficulty);
      gamePanel.add(scroll);
      gamePanel.add(lblDifficulty);
      getPicture(1);
      gamePanel.add(lblPicture);
      gamePanel.add(btnGuess);
      gamePanel.add(btnRestart);
      gamePanel.add(btnQuit);      
      gameFrame.setSize(new Dimension(470, 490));
      gameFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      gameFrame.setLayout(null);
      gameFrame.add(gamePanel);    
      gameFrame.setVisible(true);
      txtUserGuess.setEditable(false);
   }
   // gets arandom word from the dictionary text document
   public static void getWord(){
   
      try{
      
         WordList wList = (new WordList()).readFromFile("dictionary.txt");
         String list = (wList.toString()).replace("{", "");
         list = list.replace("}", "");
         wordList = list.split(", ");
      
         wordIndex = (new Random()).nextInt(wordList.length-1);// generates a random number
         int index = wordList[wordIndex].length();
         UserGuess = new String[index];
         
         for(int i = 0; i < UserGuess.length; i++){
            
            UserGuess[i] = "-";
            txtAFeedBack.append("-");
         }
      }
      catch(Exception e){};
   }
   public static void main(String[] args){
   
      try{
      
         GUI();
         //add items to the combobox
         for(int i = 1; i<12; i++){
         
            cmbDifficulty.addItem(i+"");
         
         }
       // creates a action listner for button guess  
      // which starts the game by a creating a game class object, which is the core engine of the game
         btnGuess.addActionListener(
               new ActionListener() {
                  public void actionPerformed(ActionEvent evt){
                  
                     btnGuess.setText("Guess");
                     txtUserGuess.setEditable(true);
                     if(start == true){
                           
                        
                        game.actionPerformed(evt);
                        txtUserGuess.setText("");
                     
                     
                        if(game.getWrong()){
                        
                           int difficulty = game.getLevel(Integer.parseInt(cmbDifficulty.getSelectedItem()+""));
                        
                           if(difficulty < 11){
                           
                              getPicture(difficulty);
                              gamePanel.add(lblPicture);
                           }
                           else if(difficulty >= 11){
                           
                              getPicture(11);
                              gamePanel.add(lblPicture);
                              txtAFeedBack.append("*************************\nYou Lose!!!");
                              btnGuess.setEnabled(false);
                              txtUserGuess.setEditable(false);
                           }
                        }
                     
                     }
                     else{
                     
                        start = true;
                        getWord();
                        txtAFeedBack.append("\n");
                        game  = new Game(txtUserGuess, wordList[wordIndex], txtAFeedBack, UserGuess,btnGuess);
                        System.out.println(wordList[wordIndex]);
                     }
                  }
               });
               
         // Exits the game    
         btnQuit.addActionListener(
               new java.awt.event.ActionListener() {
                  public void actionPerformed(java.awt.event.ActionEvent evt) {
                  
                     System.exit(0);
                  }
               
               }); 
               
         // Restarts the game         
         btnRestart.addActionListener(
               new java.awt.event.ActionListener() {
                  public void actionPerformed(java.awt.event.ActionEvent evt) {
                     txtAFeedBack.setText("");
                     game  = new Game(txtUserGuess, wordList[wordIndex], txtAFeedBack, UserGuess,btnGuess);
                     btnGuess.setText("Start");  
                     start = false; 
                     txtUserGuess.setEditable(false);
                     // resets the picture
                     getPicture(1);
                     game.getLevel(-1);
                     btnGuess.setEnabled(true);
                  
                  }
               
               });
      }
      catch(Exception e){
         System.out.println(e.getMessage());
      }
   }

}
