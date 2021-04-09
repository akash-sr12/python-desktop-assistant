# (c) 2020 - Akash Sarkar
# open_nix

import sys
sys.path.insert(0, 'E:/Projects/Python/myAssistant/nixAssistant/root/common/')

import os

import speak_nix as nix
import sr_nix as sr

def applications(input):
    if 'open word' in query or 'open ms word' in query or 'ms word' in query:
            nix.speak("Opening Microsoft Office Word")
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(wordPath)
            nix.speak("Done for you! Anything else for me?")

    elif 'open code' in query:
            nix.speak("Opening Microsoft Visual Studio")
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Enterprise\\Common7\\IDE\devenv.exe"
            os.startfile(codePath)
            nix.speak("Done for you! Anything else for me?")

    else: 
        nix.speak("Application not available") 
        return