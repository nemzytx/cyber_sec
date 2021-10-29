#Author : Nemuel Wainaina

#first import all the modules we are going to need in the program
import zipfile
import optparse 
import os 
from termcolor import colored
import sys
from threading import Thread

def unzip(zfile, password):
    try:
        zfile.extractall(pwd = password)
        #if success, then we found the correct password
        print(colored("[+]Found Password : " + password), "green")
        return
    except:
        #if we don't succeed, then that password is incorrect, and we simply exit from the function
        return

def main():
    #we set up the Argument Parser to be taking the values we need
    parser = optparse.OptionParser("usage%prog : zip_brute -f <zip_file>-d <password_list")
    parser.add_option("-f", dest = "zfile", type = "string", help = "Specify the Zip File")    
    parser.add_option("-d", dest = "pfile", type = "string", help = "Specify the Password File")
    (options, args) = parser.parse_args()
    
    if options.zfile == None or options.pfile == None :
        #if any of the required values are missing
        print(parser.usage)
        sys.exit(0)
    else:
        #everything's good, so now assign the values to variables we're gonna need
        zip_file = options.zfile
        pass_file = options.pfile
    
    #we check if the zip file exists at all in the first place, haha!
    if not os.path.isfile(file):
        print(colored("[-]The Zip File Does Not Exist !"), "red")
        sys.exit()
    
    #now check whether we have access to play around with the zip file
    if not os.access(file, os.R_OK):
        print(colored("[!]Access To The File Is Denied !"), "red")
        sys.exit(0)
        
    #coast clear, now create a file descriptor pointing to the zip file, the mode is read(r)
    pass_file = open(zipfile, "r")
        
    #next step is to create an object of the ZipFile class found in the zipfile module
    zfile = zipfile.ZipFile(zip_file)
    
    print(f"[+]Starting Brute Force Against File : {zip_file}\n")
    #here, we go through all the passwords in the password file or dictionary file, ...
    for password in pass_file.readlines().split("\n"):
        #for each password, we instantiate a separate thread to try extracting files from the zip file using the password
        t = Thread(target = unzip, args = (zfile, password))#create the thread
        t.start()#start the thread
    else:
        #we are supossed to print the usage menu perhaps
        pass
            

if __name__ == "__main__":
    #and now ... let her shine, haha !
    main()