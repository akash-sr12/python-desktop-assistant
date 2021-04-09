# (c) 2020 - Akash Sarkar
# win_nix

import sys
sys.path.insert(0, 'E:/Projects/Python/myAssistant/nixAssistant/root/common/')

import os
import ctypes
import time

import speak_nix as nix

def lock():
    ctypes.windll.user32.LockWorkStation()
    time.sleep(1)
    print("Your windows has been locked")
    nix.speak("Windows has been locked!")
    

def shutdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:1d}{:1d}'.format(mins, secs)
        print(timer, end="\r")
        nix.speak(timer)
        time.sleep(1)
        t -= 1
    print("Windows is shutting down!")
    nix.speak("Windows is shutting down")
    os.system("shutdown /s /t 0")
    exit()

def restart(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:1d}{:1d}'.format(mins, secs)
        print(timer, end="\r")
        nix.speak(timer)
        time.sleep(1)
        t -= 1
    print("Windows is restarting now!")
    nix.speak("Your Windows is restarting now!")
    os.system("shutdown /r /t 0")
    exit()

def logoff(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:1d}{:1d}'.format(mins, secs)
        print(timer, end="\r")
        nix.speak(timer)
        time.sleep(1)
        t -= 1
    print("Windows is logging out!")
    nix.speak("Windows is logging out")
    os.system("shutdown /l /t 0")
    exit()
