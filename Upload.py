#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
import cgi, cgitb 
import os
import Upload
import GUI
from time import perf_counter

class Upload:
    
    # Method for uploading user files to the server
    def upload(self):
        
        # Gets the path the file should be uploaded on 
        # Changes the working directory to the recieved path
        form = cgi.FieldStorage()
        keys = form.keys()
        for i in keys:
            if str(i)!='filename':
                path = str(i).replace("@", "\\")
                os.chdir(path)   
                break
        # Get filename here.
        fileitem = form['filename']
        
        # Test if the file was uploaded
        if fileitem.filename:
            # strip leading path from file name to avoid 
            # directory traversal attacks
            start_time = perf_counter()
            fn = os.path.basename(fileitem.filename)
            open(fn, 'wb').write(fileitem.file.read())
        
            message = 'The file "' + fn + '" was uploaded successfully'
            end_time = perf_counter()
            execution_time = end_time - start_time
            trials = open("C:\\xampp\htdocs\\fileman\\testing.txt",'a')
            trials.writelines("\n"+str(execution_time))
            trials.close()             
        else:
            message = 'No file was uploaded'
    
    def main():
        up = Upload.Upload()
        up.upload()
        gui = GUI.GUI()
        gui.layout()        
    
    if __name__=="__main__":
        main()        
