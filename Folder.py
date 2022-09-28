import os
import shutil
from FileItem import FileItem

class Folder(FileItem):
    def __init__(self, path):
        super().__init__(path)
        
    # Deleting a directory
    def deleteDir(self):
        
        if os.path.isdir(self.path):  
            shutil.rmtree(self.path)
        else:
            message ="Directory does not exist"    
     # Creates a new directory 
     # The path parameter is the path where the new folder will be created in
     # The name parameter is the name of the folder
     # The typ is the type folder
     # The method changes the working directory to the path in path parameter
     # Then it creates the new directory
    def create(self, path,name,typ):
        
        os.chdir(path)
        try:
            os.mkdir(name)
            return True
            
        except:
            return typ+" already exists"
        

