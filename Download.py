#!C:\Users\Ndira\AppData\Local\Programs\Python\Python36\python.exe
import cgi
import Download


class Download:
    
    #  Downloads the file in the path variable which is obtained from cgi storage
    def download(self):
        
        # Creates a download link for the file
        # The path is preproccessed before downoading the file
        path = str(cgi.FieldStorage().getvalue('name')).replace("@","\\")
        print("Content-type:text/html\r\n\r\n ")
        temp = path.split("\\") # gets exact file name i.e separates it from the full path
        print("<a href="+'"'+path+'"'+" download> CLick this link to download "+temp[len(temp)-1])
        
    def main():

        dl = Download.Download()  
        dl.download()
    
    if __name__ == "__main__":
        main()