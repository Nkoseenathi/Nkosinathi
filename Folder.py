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
            
    # Copying directory
    def copyDir(self,src, dst):
    
        if os.path.isdir(src):
            shutil.copytree(src, dst+src[1:])
            message ="Directory has been copied"
        else:
            message ="Directory does not exist"
            
    def create(self, dst,name):
        
        os.chdir(dst)
        try:
            os.mkdir(name)
            return True
            
        except:
            return "Username already exists"
