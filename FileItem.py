import os
import shutil

class FileItem:
    def __init__(self, path):
        self.path = path
        
    def getSize(self):
        return os.stat(self.path);
    
    def getName(self):
        return self.path
    
    def rename(self,destination):
        message = ""
        if os.path.isfile(destination) or os.path.isdir(destination):
            os.rename(self.path,destination)
            message = "File renamed successfully"
            
        else:
            message = "File not renamed successfully"   
        return message
            
            
    def move(self,destination):
        message = ""
        if os.path.isfile(destination) or os.path.isdir(destination):
            shutil.move(self.path, destination)
            message = "File moved successfully"
            
        else:
            message = "File not moved successfully"   
        return message        
        