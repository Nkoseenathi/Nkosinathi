#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
import FileOperations
import glob
import cgi, cgitb 


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
   FileOperations.deleteFile(path)

# "Refresh the GUI page"
exec(open("GUI.py").read())


   
   