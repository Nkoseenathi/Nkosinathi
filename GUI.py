#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
# Import modules for CGI handling
import glob
import os
import cgi
import cgitb
import GUI
import Login


class GUI:
    
    def login(self,message):
     
        if message!="":
            print("Content-type:text/html\r\n\r\n ")
            print("""
            <script src="route.js"></script>
            <form action = "Login.py" method = "get">
         First Name: <input type = "text" name = "username">  
         <br />
         Last Name: <input type = "text" name = "password" />
         <br/>
         <a name="create" href="javascript:create()">Create new account</a>
         <br/>
         <input type = "submit" value = "Login" />
         <br />
         """+message+"""
         </form>""")
        else:
            print("Content-type:text/html\r\n\r\n ")
            print("""
            <script src="route.js"></script>
            <form action = "Login.py" method = "get">
         First Name: <input type = "text" name = "username">  
         <br />  
         Last Name: <input type = "text" name = "password" />
         <br/>
         <a name="create" href="javascript:create()">Create new account</a>
         <br/>
         <input type = "submit" value = "Login" />
         </form>""")        
        
    def create(self,message,err):

        if message=="create":
            
            print("Content-type:text/html\r\n\r\n ")
            print("""<form action = "Login.py?" method = "get">
         First Name: <input type = "text" name = "username">  
         <br />
         Password: <input type = "text" name = "password" />
         <br />
         Confirm : <input type = "text" name = "confirm" />
         <br />"""+err+"""
         <br />
         <input type = "submit" value = "Create" />
         </form>""")
            
        elif message == False:
            
            print("Content-type:text/html\r\n\r\n ")
            print("""<form action = "Login.py" method = "get">
         First Name: <input type = "text" name = "username">  
         <br />
         <a name="create" href="javascript:create()">Create new account</a>
         Last Name: <input type = "text" name = "password" />
         <br/>
         <input type = "submit" value = "Login" />
         <br />
         """+message+"""
         </form>""")   
        
        else:
            
            gui = GUI.GUI()
            gui.layout()             
        
    def layout(self):

        path = cgi.FieldStorage()
        if (str(path.getvalue('path'))) != "None":
            path = str(path.getvalue('path')).replace("@", "\\")
            os.chdir(path)

        userFolder = glob.glob(".\\*")
        normalized_path = os.path.normpath(os.getcwd())
        path_components = normalized_path.split(os.sep)
        paths = self.pathBuilder(os.getcwd())

        print("""Content-type:text/html\r\n\r\n
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/all.min.css" integrity="sha256-2XFplPlrFClt0bIdPgpz8H7ojnk10H69xRqd9+uTShA=" crossorigin="anonymous" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/4.5.6/css/ionicons.min.css" integrity="sha512-0/rEDduZGrqo4riUlwqyuHDQzp2D1ZCgH/gFIfjMIL5az8so6ZiXyhf1Rg8i6xsjv+z/Ubc4tt1thLigEcu6Ug==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
        <link rel="stylesheet" href="style.css"/>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" />
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
        <script src="route.js"></script>
 
  
           

        <div class="container flex-grow-1 light-style container-p-y">
          <div class="container-m-nx container-m-ny bg-lightest mb-3">
            <ol class="breadcrumb text-big container-p-x py-3 m-0">""")
        for i in range(5, len(paths)):

            print("""<li class="breadcrumb-item">""")
            print("""<a href="javascript:locate(`"""+paths[i]+'`)">'+path_components[i]+"</a>")
            
        print("</li>")

        print("""
             </ol>
             
            <table class="table"> 
             <tr><div>
            <form enctype = "multipart/form-data" 
                              action = "Upload.py" method = "post">
            <p>File: <input type = "file" name = "filename" /></p>
            <p><input type = "submit" name =""" +'"'+os.getcwd()+'"' +""" value="Upload" class="btn btn-primary mr-2"/><i class="ion ion-md-cloud-upload"></i></p>
            </form>
            </div></tr>
            
             <hr class="m-0" />
        
        <div class="file-manager-actions container-p-x py-2">
         <div class="file-manager-container file-manager-col-view">
             <div class="file-manager-row-header">
                 <div class="file-item-name pb-2">Filename</div>
                 <div class="file-item-changed pb-2">Changed</div>
             </div>""")
        
             
        # Print all the user files
        for i in userFolder:
            # Diplays the the files the given folder which is stored in userFolder
            print("""
   
           <div class="file-item">
                <div class="file-item-select-bg bg-primary"></div>
                <label class="file-item-checkbox custom-control custom-checkbox">
                    <input type="checkbox" class="custom-control-input" />
                    <span class="custom-control-label"></span>
                </label>""")
            print(self.fileType(i[2:]))

            print("""<a name="file-item" class="file-item-name" href="""+""""javascript:go_to(`""" +
                  str(os.getcwd()).replace("\\", "@")+"@"+i[2:]+"""`)">"""+i[2:]+"</a>")  # Display the file name
            print(" <form action = \"FormHandler.py\" method = \"post\" target = \"_blank\">")   # Specify the file that is going to perfom the form action
            # print("<input type = \"submit\" name="+i.replace(" ","^")+" value = \"Commit\"/> </form> ") # Since names with more than one word don't get passed replace the spaces with a character to make the name a single word
            print("""          
        </div>
        

        """)
        print("</html>")

    def viewer(self, path,typ):
        
        path = path
        name = str(path).split("\\")
        name = name[len(name)-1]
        path = path[:-len("\\"+name)]
        os.chdir(path)
        path = name


        if(typ=="text"):
            
            print("Content-type:text/html\r\n\r\n ")
            with open(path) as f:
    
                for i in f:
                    print(i+"\n")
                    
        elif typ == "video":
            
            print("Content-type:text/html\r\n\r\n ")
            print("""  
            <video width="600" height="400" controls> 
            <source src="""+'"'+path+'"'+""" type="video/ogg">
              <source src="""+'"'+path+'"'+""" type="video/mp4">
            Your browser does not support the video tag.
            </video>""")
           
        elif typ =="audio":
            
            print("Content-type:text/html\r\n\r\n ")
            print(""" 
            
            <audio controls>
              <source src="""+'"'+path+'"'+""" type="audio/ogg">
              <source src="""+'"'+path+'"'+""" type="audio/mpeg">
            Your browser does not support the audio element.
            </audio>""")
        
        elif typ == "image":
            print("Content-type:text/html\r\n\r\n ")
            print("""
            <html>
           <head>
              <title>"""+path+"""</title>
           </head>
        
           <body>
              <img src="""+'"'+path+'"'+""" alt="Image type not supported" width="800" height="500">
           </body>
        </html>""")
                    
    def fileType(self,name):
        
        if os.path.isdir(".\\"+name):
            return """ <div class="file-item-icon far fa-folder text-secondary"></div>"""
            
        if str(name[-3:])in ('mp3|ogg|wav'):
            return """ <div class="file-item-icon far fa-file-audio text-secondary"></div>"""
        
        if str(name[-3:]) in ('avi|mp4|flv'):
            return """<div class="file-item-icon far fa-file-video text-secondary"></div>"""
        
        if str(name[-3:]) in ('jpg|png|gif'):
            return """<div class="file-item-img" style="background-image: url(https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-image-512.png);"></div>""" 
        
        if str(name[-3:])in ('txt|pdf|rtf'):
            return """<div class="file-item-icon far fa-file-alt text-secondary"></div>"""
                                                 
        return """<div class="file-item-icon far fa-file text-secondary"></div>"""
    
    def pathBuilder(self, path):
        normalized_path = os.path.normpath(path)
        path_components = normalized_path.split(os.sep)
        builder = []
        builder.append(path_components[0])
        for i in range(1, len(path_components)):
            builder.append(builder[i-1]+"@"+path_components[i])
        return builder

    def main():

        gui = GUI.GUI()  # Create an object of the GUI class
        if str(cgi.FieldStorage().getvalue('action')) == "create":
            gui.create("create","")  
            
        elif str(cgi.FieldStorage().getvalue('path')) == "None":
            
            gui.login("")  # Diplay user interface and the all file in the top directory of the user
  
        else:
            gui.layout()



    if __name__ == "__main__":
        main()
