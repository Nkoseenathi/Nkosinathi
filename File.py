import glob
import os
import shutil
from Files import Files

class File(Files):

  def __init__(self, path):
    super().__init__(path) 
    
  message = ""
  
  #Deleting a file
  def deleteFile(self):
    
    if os.path.isfile(self.path):
      os.remove(self.path)
      message= "File has been deleted"
    else:
      message ="File does not exist"
      
  # Copying a file  
  def copyFile(original,target):
    
    if os.path.isfile(original):
      shutil.copyfile(original, target+original[1:])
      message ="File has been copied"
    else:
      message ="File does not exist" 
    


  

