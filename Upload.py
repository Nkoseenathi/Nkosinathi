#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
import cgi, cgitb 
import os
form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid 
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open(fn, 'wb').write(fileitem.file.read())

    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'
    
# "Refresh the GUI page"
exec(open("GUI.py").read())
