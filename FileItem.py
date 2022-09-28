import os
import shutil

class FileItem:
    
    def __init__(self, path):
        self.path = path
        

    # Copies a file item to given destination
    # The dst parameter is the destination of the file item
    # the temp variable holds the name of the file item
    # Checks if the file item is file or folder to apply the correct code
    # The name in temp is appended to the destination so that file item will be copied to that destination 
    def copy(self,dst):
        temp = self.path.split("\\");
        if os.path.isdir(self.path):
            shutil.copytree(self.path, dst+"\\"+temp[len(temp)-1])
            
        if os.path.isfile(self.path): 
            shutil.copyfile(self.path, dst+"\\"+temp[len(temp)-1])
    
    # Renames the file item to the given in the nname parameter
    def rename(self,nname):
        
        os.rename(self.path,nname)
         
      # Moves the file to the given destination in the destination   parameter    
    def move(self,destination):
        shutil.move(self.path, destination)
       
            
        
        

            
      
        