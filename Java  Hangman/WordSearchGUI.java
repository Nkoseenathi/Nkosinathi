import javax.swing.*;
import java.awt.*;

public class WordSearchGUI extends JFrame{

   JTextField txfPattern;
   JTextArea  txaMatches;
   JButton btnSearch;
   JLabel lblInfo;
   WordList wordList;
   JPanel wsPanel;
   
   public WordSearchGUI(){
   
      wordList = new WordList();
      setSize(350,330);
      setTitle("Word Puzzle Solver");
      wsPanel = new JPanel();
      lblInfo = new JLabel("Enter a pattern or word on the textbox below");
      wsPanel.setPreferredSize(new Dimension(350, 330));      
      wsPanel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createLineBorder(Color.black)));
      wsPanel.setBounds(20, 20, 430, 410);
      wsPanel.setLayout(null);
      txaMatches = new JTextArea();
      txfPattern = new JTextField();
      txaMatches.setEditable(false);
      btnSearch = new JButton("Search");
      txfPattern.setBounds(20,50,170,30);
      lblInfo.setBounds(20,-80,280,200);
      btnSearch.setBounds(200,50,80,30);
      
    
   
      PatternMatcher pm = new PatternMatcher( txfPattern, wordList, txaMatches);
      
      
      JScrollPane scrollPane = new JScrollPane(txaMatches);
      scrollPane.setBounds(20,100,170,170);
      
      wsPanel.add(lblInfo);
      wsPanel.add(txfPattern);
      wsPanel.add(btnSearch);
      wsPanel.add(scrollPane);
      add(wsPanel);
     
      btnSearch.addActionListener(pm);
      setDefaultCloseOperation(EXIT_ON_CLOSE);
   }
   
   public static void main(String args[]){
   
      WordSearchGUI one = new WordSearchGUI();
      one.setVisible(true);
      
   }
}