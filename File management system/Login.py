#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
import cgi, cgitb 
import os
import Login
import GUI
import Folder

class Login:
      
   def check(self):
      
      details = cgi.FieldStorage()
      username = details.getvalue('username')
      password  = details.getvalue('password')       
      
      login = False
      gui = GUI.GUI()
      # Checks if the username and password are in the users file
      # If they are in file it changes the working directory to the username so that the user files will be displayed on the screen
      # If they are not in the system it returns an error message
      
            
      with open("users.txt") as l:
         
         for i in  l:
           
            temp = str(i).split(" ")

            if(str(temp[0]).strip()==username and str(temp[1]).strip()==str(password).strip()):
               login = True
               os.chdir(".\\users\\"+username)
               gui.layout() 
                         
               break
         
      if login == False:
         gui.login("Invalid username or password")
         
   def create(self):
      
      gui = GUI.GUI()
      details = cgi.FieldStorage()
      username = details.getvalue('username')
      password  = details.getvalue('password') 
      confirm = details.getvalue('confirm') 
      # Checks if password is the same as confirmation password 
      # If they are not the same it returns an error message
      if confirm != password:
         gui.create("Passwords don't match")
         
      else:
         
            # If they are the same it will create a new folder that is named using the username
            # The folder class will raise an error if the folder name exist and the user will have to enter a new username
           # If the username is not taken the username and password will be appended to the users text file
         folder = Folder.Folder(username)
         msg = folder.create("C:\\xampp\\htdocs\\fileman\\Users",username,"Username")
      
         if msg == True:
            users = open("C:\\xampp\\htdocs\\fileman\\users.txt","a")
            users.write("\n"+username+" "+password)            
            os.chdir(".\\"+username)
            gui.layout() 
         else:
            gui.create("Username is taken")
      
      

      
   def main():
      
      lg = Login.Login() 
      if str(cgi.FieldStorage().getvalue('confirm')) !="None":
         lg.create()
      else:
         lg.check()
       

   if __name__=="__main__":
      main()           