# (c) 2020 - Akash Sarkar
# greeting_nix

import sys
sys.path.insert(0, 'E:/Projects/Python/myAssistant/nixAssistant/root/common/')

import datetime

import speak_nix as nix

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        nix.speak("Good Morning")

    elif hour>=12 and hour<18:
        nix.speak("Good Afternoon")   

    else:
        nix.speak("Good Evening")  

    nix.speak("Akash! How may I help you?")
