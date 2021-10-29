#Author : Nemuel Wainaina

import pyautogui
import os
from datetime import datetime as dt
import time

current_date = dt.now().strftime("%x").replace("/", "_")#replacement of / with _ is to avoid any conflicts that may arise
#due to the use of / in file paths as well
#set the path to a relevant one according to your file system
path_to_save = "D:\\MyProjects\\Other_Py\\ScrShots\\"
capture_after_every = 60
counter = 1

def get_last_scrshot():
    #the purpose of this function is to solve any conflicts that may arise
    #in generating and assigning names to the screenshots as they get saved onto the system
    #
    counter_posn = 1
    last_scrshot = ""
    for file in os.listdir(path_to_save):
        if file.split(".")[-1] == "jpg" and int(file.split(".")[0].split("_")[-1]) > counter_posn :
            counter_posn = int(file.split(".")[0].split("_")[-1])
            last_scrshot = str(file)
    return last_scrshot, counter_posn

def scrshot():
    global counter
    myscrshot = pyautogui.screenshot()
    path_name = path_to_save + f"/{current_date}_{counter}.jpg"
    if os.path.exists(path_name):#to check whether there are other files in the folder
        #if yes, then let's find the last one, get it's file name and also
        #extract the counter position from it's name
        last_scrshot, last_counter_posn = get_last_scrshot()
        counter = last_counter_posn
    myscrshot.save(path_name)
    counter = counter + 1
    #recursive function, whaaat!
    #yeah, it's just it, not kidding
    time.sleep(capture_after_every)#comment this line and the code will run non-stop
    #and that's quite not necessary, there's not much we can expect to have changed within that shoooort time
    #and so we use the sleep function
    scrshot()
    
    
while True:
    #quite interesting way to start, right? Haha!
    scrshot()

    
    
    