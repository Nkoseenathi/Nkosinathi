import glob
import os
import shutil


message = ""

#Deleting a file
def deleteFile(path):
  if os.path.isfile(path):
    
    os.remove(path)
    message= "File has been deleted"
    
  else:
    message ="File does not exist"
    i=0
  
# Deleting a directory
def deleteDir(path):
  if os.path.isdir(path):  
    shutil.rmtree(path)
    
  else:
    message ="Directory does not exist"
    
# Copying a file  
def copyFile(original,target):
  if os.path.isfile(original):
    
    shutil.copyfile(original, target+original[1:])
    message ="File has been copied"
    
  else:
    message ="File does not exist" 
  

# Copying directory
def copyDir(src, dst):
  
  if os.path.isdir(src):
    
    shutil.copytree(src, dst+src[1:])
    message ="Directory has been copied"
    
  else:
    message ="Directory does not exist"
  

