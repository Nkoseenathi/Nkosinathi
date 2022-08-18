#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
import glob
import os
import cgi, cgitb
from File import File
from Folder import Folder

path = ""
form = cgi.FieldStorage() 
# Get selected value on the dropdown box
if form.getvalue('dropdown'):
   selection = form.getvalue('dropdown')
   path = form.keys()
   
else:
   selection = "Not entered"
   
# Get path of the selected file 
for i in path:
   if i!="dropdown":
      path = i.replace("^", " ")
      
# Delete file      
if selection == "Delete":
   
   if(os.path.isfile(path)):
      file = File(path)
      file.deleteFile()
   else:
      folder = Folder(path)
      folder.deleteDir()
   
   

# "Refresh the GUI page"
exec(open("GUI.py").read())


   
   