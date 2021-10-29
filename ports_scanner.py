#Author : Nemuel Wainaina

#This program takes the target from the users and performs port scanning on the specified target/s 
#could be one or more targets
#Also, the user specifies the number of ports he or she intends to scan or check whether they are open

#import the required libraries first
import socket
from IPy import IP
from termcolor import colored
#the purpose of this library(termcolor) is to add some color to our code

def scan(target):
    cvted_ip = check_ip(target)
    print()#insert a blank line
    print("[+]Scanning Target : " + str(target))
    print()#insert a blank line
    for port in range(ports+1):
        scan_target(target, port)

def check_ip(ip):
    '''This function is aimed at accomodating both ways of referring to the target
    could be by using the hostname or just the ip address'''
    try:
        #this function returns true if the passed value is an IP Address
        #else a ValueError is raised
        IP(ip)
        return ip
    #here we now handle the ValueError
    except ValueError:
        return socket.gethostbyname(ip)
    
def scan_target(target, port):
    try:
        #create our socket object
        sock = socket.socket()
        #this section is optional, I have set it this way in order for the program to be a bit more fast in responding
        #however, the higher the timeout the better the accuracy and the vice versa is also true
        sock.settimeout(0.5)
        #now try connecting to the target machine over the specified port
        sock.connect((target, port))
        #if successful then go on into the try...except...
        #otherwise move on to the except section at the end of this function
        try:
            #we grab the banner if any, hence the recv function is called
            banner = sock.recv(1024)
            print(colored("[+]Port " + str(port) + " is open : " + str(banner.decode().strip("\n").strip("\r")), "green"))
        except:
            #this is if we do not manage to grab the banner
            print(colored("[+]Port " + str(port) + " is open", "green"))
    except:
        #if the port is closed
        #print("[+]Port " + str(port) + " is closed")
        #we do not really need the ports which are closed, so we just pass
        pass
    
    
#we include this to make sure that the code in this section is only executed when we are running the file on its own
#and make sure that the code will not be executed should we import this file as a module in another file
if __name__ == "__main__":
    #ask the user for the target/s and the number of ports to scan
    targets = input(("[+]Enter Target/s To Scan(Separate multiple targets with a comma) : "))
    ports = int(input("[+]Enter The Number Of Ports To Scan(eg. 500 means the first 500 ports) : "))
    if "," in targets:
        for target in targets.split(","):
            scan(target)
    else:
        #the targets are one, so we just go ahead and scan the one target directly
        scan(targets)
                
    
