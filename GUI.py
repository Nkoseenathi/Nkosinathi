#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
# Import modules for CGI handling 
import glob
import cgi, cgitb 
paths = glob.glob(".\\*")
print ("Content-type:text/html\r\n\r\n")


print("""
    <body>
   <form enctype = "multipart/form-data" 
                     action = "upload.py" method = "post">
   <p>File: <input type = "file" name = "filename" /></p>
   <p><input type = "submit" value = "Upload" /></p>
   </form>
</body>
    """)
for i in paths: 

    print("<a name=\"file-item\" onsubmit=\"refreshPage()\" href=\"javascript:void(0)\">"+i[2:]+"</a>")    
    print(" <form action = \"FormHandler.py\" method = \"post\" target = \"_blank\">")
    print("""<select name = "dropdown">
    <option value = "Delete" selected>Delete</option>
    <option value = "Copy">Copy</option>
    <option value = "Move">Move</option>
    <option value = "Rename">Rename</option>
    <script type='text/javascript'>
    function refreshPage(){
    console.log("Refreshing page");
    location.reload ? location.reload() : location = location;
    }
    </script>
    </select>""")
    print("<input type = \"submit\" name="+i.replace(" ","^")+" value = \"Commit\"/> </form> ")
print ("</html>")
    
