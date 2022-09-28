#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
# Import modules for CGI handling
import glob
import os
import cgi
import cgitb
import GUI
import Login
import Folder, File



class GUI:
    
    # This methods generates the login html for displaying the login screen to the user
    # The message parameter displays the error message if the user entered the wrong details
    # It is initially empty if the user is logging in for the first time
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
         <a name="create" href="javascript:createUser()">Create new account</a>
         <br/>
         """+message+"""
         <input type = "submit" value = "Login" />
         
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
         <a name="create" href="javascript:createUser()">Create new account</a>
         <br/>
         <input type = "submit" value = "Login" />
         </form>""")        
      
     # This methods generates the html for creating a new account which will be displayed to the browser
     # The error parameter diplays an error if the was a problem creating a new account
    def create(self,err):
         
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
        
    def layout(self):
        # Gets the path from cgi storage and change the working directory to the path recieved
        # Javascrips gives an error for paths that contain backslash so the backslash is replaced by @ when it is passed to the html page
        # When the path is passed back to the system for processing it reverted back to the backslashes 
        path = cgi.FieldStorage()
        if (str(path.getvalue('path'))) != "None":
            path = str(path.getvalue('path')).replace("@", "\\")
            os.chdir(path)

        # After changing the working directory all the file items are stored in the userFolder the list of the files is obtained using glob module
        # The path is broken down to componets to separate the folder name from the path so that it will be displayed correctly to the user
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
        
        # Displays a navigation bar which consist of links of parent directories of the current directory the user is in.
        # Start from 5 to restrict the user from navigating to folders in the server that they shouldn't have access to e.g accessing other users folders or files in the server that do not belong to them
        for i in range(5, len(paths)):

            print("""<li class="breadcrumb-item">""")
            print("""<a href="javascript:locate(`"""+paths[i]+'`)">'+path_components[i]+"</a>")
            
        print("</li>")

        # Displays a form which contains the upload button and the file chooser
        # Also displays the move,create copy and logout button 
        print("""
             </ol>
             
            <table class="table"> 
             <tr><div class="child inline-block-child">
            <form enctype = "multipart/form-data" 
                              action = "Upload.py" method = "post">
            <p>File: <input type = "file" name = "filename" /></p>
            <p><input type = "submit" name =""" +'"'+os.getcwd()+'"' +""" value="Upload" class="btn btn-primary mr-2"/><i class="ion ion-md-cloud-upload"></i></p>
            </form>
            </div></tr>
            <div class="child inline-block-child"> <input type = "submit" onclick="javascript:create(`"""+str(os.getcwd()).replace("\\","@")+"""`)" value="Create new foder" > </div>
            <div class="child inline-block-child"> <input type = "submit" value="Move" onclick="javascript:move(`"""+str(os.getcwd()).replace("\\","@")+"""`)"> </div>
            <div class="child inline-block-child"> <input type = "submit" value="Copy" onclick="javascript:copy(`"""+str(os.getcwd()).replace("\\","@")+"""`)"> </div>
            <div class="child inline-block-child"> <input type = "submit" onclick="javascript:logout()" value="Logout"> </div>
            
             <hr class="m-0" />
        
        <div class="file-manager-actions container-p-x py-2">
         <div class="file-manager-container file-manager-col-view">
             <div class="file-manager-row-header">
                 <div class="file-item-name pb-2">Filename</div>
                 <div class="file-item-changed pb-2">Changed</div>
             </div>""")
        
             
        # Print all the user files in the current working directory
        for i in userFolder:
            
            print("""
   
           <div class="file-item">
                <div class="file-item-select-bg bg-primary"></div>
                <label class="file-item-checkbox custom-control custom-checkbox">
                    <input type="checkbox" class="custom-control-input" />
                    <span class="custom-control-label"></span>
                </label>""")
            # Gets the file extenstion and determines the file type so that a proper icon will be displayed for the file 
            fileType = self.fileType(i[2:])
            print(fileType)
            # Modify the file item path so that the files can be accessed by the browser when running the server as the browser doesnt allow access of file stored locally in the machine
            # truncate the local part of the file item and make the path start from the server name e.g C:\Nkosinathi\server\users\Nkosi ---> .\users\Nkosi
            wd = str(os.getcwd())
            try:
                index = wd.index("users")
            except:
                index = wd.index("Users")
            name = "\\"+wd[index:]     
            txtName = "."+name+"\\"+i[2:]
            name = name.replace("\\", "@")+"@"+i[2:]
            # Add dropdown item to the file item
            
            print(""" <div class="file-item-actions btn-group">
                <button type="button" class="btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle" data-toggle="dropdown"><i class="ion ion-ios-more"></i></button>
                <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" href="""+""""javascript:rename(`""" +
                  name+"""`)">Rename</a>""")
            print("""<a class="dropdown-item" href="""+""""javascript:move(`""" +
                  name+"""`)">Move</a>""")
            print("""<a class="dropdown-item" href="""+""""javascript:copy(`""" +
                  name+"""`)">Copy</a>""")
            print("""<a class="dropdown-item" href="""+""""javascript:fdelete(`""" +
                  name+"""`)">Delete</a>""")      
            print("""<a class="dropdown-item" href="""+""""javascript:download(`""" +
                  name+"""`)">Download</a></div></div> """) 
            
            # Dont use javascript for text documents as they can be viewed by the browser automatically and dont have to be processed first
            if fileType == """<div class="file-item-icon far fa-file-alt text-secondary"></div>""" or fileType == """<div class="file-item-icon far fa-file text-secondary"></div>""" :
            
                print("""<a name="file-item" class="file-item-name" <a href="""+'"'+txtName+'"'+" )>"+i[2:]+"</a>") # Display the file name
            else:
                print("""<a name="file-item" class="file-item-name" href="""+""""javascript:go_to(`""" +
                      name+"""`)">"""+i[2:]+"</a>")  # Display the file name
            print("""          
                     </div>
                     
             
                     """)
        print("</html>")

    # Determines how a file is going to be opened based on its file type
    # The typ parameter is used to determine the view
    # The path parameter is the path of the file to be viewed
    def viewer(self, path,typ):

        name = str(path).split("\\")
        name = name[len(name)-1]
        path = path[:-len("\\"+name)]
        os.chdir(path)
        path = path+"\\"+name
        


        if typ == "video":
            
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
     
     # Determines a file by its extenstion or by checking if its a directory and return the icon of the file based on its type               
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
   # Preprocesses the path of a file to be renamed and call the rename method to rename the file item
   # The path parameter is the path of the file to be renamed and it contains @ instead of \ hence it needs to be preproccessed
   # nname is the new name of the file item to be renamed
   
    def rename(self, path,nname):
        
 
        name = str(path).split("@")
        path = path.replace("@","\\")
        name = name[len(name)-1]
        path = path[:-len("\\"+name)]
        os.chdir(path)
        
        folder = Folder.Folder(".\\"+name)
        folder.rename(".\\"+nname)
        self.layout() # Refreshes the page to show new name of the file item
   
    # Preprocesses the path that the folder is going to be created on and calls the folder create method craate a new folder   
    # The path the new folder is going to be created on
    # The name of new folder
    # type: the type of folder that is going to be created 
    def createFolder(self, path,name,typ): 
        
        path = str(path).replace("@","\\")
        if(typ == "Username"):
            name = str(path).split("@")
            name = name[len(name)-1]
        folder = Folder.Folder(name)
        folder.create(path,name,typ)
        self.layout()        
        
         
    
    # Breaks down a path of a nested subfolder into separate parent folders and stores them in a list
    # The path parameter is the subfolder path that is going to be broken down
    def pathBuilder(self, path):
        normalized_path = os.path.normpath(path)
        path_components = normalized_path.split(os.sep)
        builder = []
        builder.append(path_components[0])
        for i in range(1, len(path_components)):
            builder.append(builder[i-1]+"@"+path_components[i])
        return builder
    
  # The main method gets data from cgi storage Preprocesses the data, calls the method/object to handle the recieved data and diplays the output based on the method/object
    def main():

        gui = GUI.GUI()  # Create an object of the GUI class
        ui = str(cgi.FieldStorage().getvalue('action'))

        if  ui == "create":
            gui.create("")  
            
        elif ui == "createD":# create directory
           
            name = str(cgi.FieldStorage().getvalue('name'))
            path = str(cgi.FieldStorage().getvalue('path'))
            gui.createFolder(path,name,"Folder name")
            
    
        
        elif ui == "delete":

            name = str(cgi.FieldStorage().getvalue('name'))
            path = name
            name = str(path).split("@")
            path = path.replace("@","\\")
            name = name[len(name)-1]
            path = path[:-len("\\"+name)]
            os.chdir(path)            
            if len(str(name).split(".")) == 1:
                folder = Folder.Folder(".\\"+name)
                folder.deleteDir()
            else:
                file = File.File(".\\"+name)
                file.deleteFile()  
            gui.layout()
                
            
        
        elif ui == "rename":
            
            name = str(cgi.FieldStorage().getvalue('name'))
            nname = str(cgi.FieldStorage().getvalue('nname'))            
            gui = GUI.GUI()
            gui.rename(name,nname)
       
            
        
        elif ui == "move" or ui == "copy":
            
            temp = open("C:\\xampp\\htdocs\\fileman\\"+ui+".txt")
            line = str(temp.readline())
            if  line=='':
                
                temp.close()
                name = "."+str(cgi.FieldStorage().getvalue('name')).replace("@","\\")
                tname = str(name).split("\\")
                tname = tname[len(tname)-1]
                path = name[:-len("\\"+tname)]  
                os.chdir(path)
                temp = open("C:\\xampp\\htdocs\\fileman\\"+ui+".txt",'w')
                temp.write(os.path.abspath(".\\"+tname))
                temp.close()
                
            else:
                
                temp = open(r"C:\\xampp\\htdocs\\fileman\\"+ui+".txt")
                name = line.strip()
                nname = str(cgi.FieldStorage().getvalue('name')).replace("@","\\")
                os.chdir(nname)
                folder = Folder.Folder(name)
                if(ui=="move"):
                    folder.move(nname)
                else:
                    folder.copy(nname)
                   
                temp = open("C:\\xampp\\htdocs\\fileman\\"+ui+".txt","r+")
                temp.truncate(0) # clears the file
                temp.close()
                
            gui.layout()
            
            
        elif ui =="path":
            gui.layout()        
                
        elif ui == "None":
            
            gui.login("")  # Diplay the login screen
            
  
        else:
            gui.layout()



    if __name__ == "__main__":
        main()
