# (c) 2020 - Akash Sarkar
# sr_nix

import speech_recognition as sr
import time
import os

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #os.system('cls')
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        #os.system('cls')
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
        time.sleep(1)

    except Exception as e:
        #os.system('cls')
        #print(e)
        print("Say that again please...")
        time.sleep(1)
        return "none"
    return query
