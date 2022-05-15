import imp
import os
import string
import pyautogui
import time


def openfile() :
    os.startfile('hack.txt')
    pyautogui.Pause=0.1
    string="""Hi Naresh I'M Hack Your System
                Dont Worry 
                You Cant Retwrie
                
                Call To....{6369129144}."""
    time.sleep(2)
    for i in str(string) :
    #    os.startfile('hack.txt')
        time.sleep(1)
        pyautogui.hotkey(str(i))

        time.sleep(2)

openfile()
