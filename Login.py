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
      if confirm != password:
         gui.create("create","Passwords don't match")
         
      else:
         
         folder = Folder.Folder(username)
         msg = folder.create("C:\\xampp\\htdocs\\fileman\\Users",username)
         
         if msg == True:
            users = open("C:\\xampp\\htdocs\\fileman\\users.txt","a")
            users.write("\n"+username+" "+password)            
            os.chdir(".\\"+username)
            gui.layout() 
         else:
            gui.create("create","Username is taken")
      
      

      
   def main():
      
      lg = Login.Login() 
      if str(cgi.FieldStorage().getvalue('confirm')) !="None":
         lg.create()
      else:
         lg.check()
       

   if __name__=="__main__":
      main()           