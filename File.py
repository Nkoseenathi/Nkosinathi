#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
import glob
import os
import cgi, cgitb 
import GUI
import File
import shutil
from FileItem import FileItem

# Constructor 
# File class is a base class of fileItem
class File(FileItem):

  def __init__(self, path):
    super().__init__(path) 
    
  message = ""
  
  #Method for  deleting a file
  def deleteFile(self):
    
    if os.path.isfile(self.path):# Checks if the file exists
      os.remove(self.path) # Deletes the file
      message= "File has been deleted"
    else:
      message ="File does not exist"
      
   # Opens the file     
   #  The path parameter is the path of the file to be opened 
   # The typ parameter is the type of file to be opened 
   # The viewer method in GUI is displayed to generate a html page that wil display the file
  def openF(self,path,typ):
    
    gui = GUI.GUI() 
    gui.viewer(path,typ)
    
  def main():
    
    loc = cgi.FieldStorage()
    typ = str(loc.getvalue('typ'))
    loc = str(loc.getvalue('path')).replace("@", "\\")
    file = File.File(loc) #Create an object of the File class
    file.openF(loc,typ)
  
  if __name__=="__main__":
    main()    
    
    


  

