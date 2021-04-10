# (c) 2020 - Akash Sarkar
# nixAssistant
# MIT License

import sys
sys.path.insert(0, 'E:/Projects/Python/myAssistant/nixAssistant/root/')

import wikipedia
import webbrowser
import os
import random
import time
import requests, json
import common.speak_nix as nix
import common.sr_nix as sr
import greeting_nix
import win_nix
import weather_nix
import news_nix
import covid19_nix
import email_nix
import test_nix


if __name__ == "__main__":
    greeting_nix.wishMe()
    while True:
        query = sr.takeCommand().lower()

        if "who are you" in query:
            print("I'm nix, a personal assistant made by Mr Akash.")
            nix.speak("I'm nix, a personal assistant made by Mr Akash.")

        elif 'wikipedia' in query:
            nix.speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            nix.speak("According to Wikipedia")
            print(results)
            nix.speak(results)

        elif 'open youtube' in query:
            nix.speak("Opening youtube.com")
            webbrowser.open("youtube.com")
            nix.speak("Anything else for me?")

        elif 'open google' in query:
            nix.speak("Opening google.com")
            webbrowser.open("google.com")
            nix.speak("Anything else for me?")

        elif 'open stackoverflow' in query:
            nix.speak("Opening stackoverflow.com")
            webbrowser.open("stackoverflow.com")   
            nix.speak("Done for you! Anything else for me?")

        elif 'open facebook' in query:
            nix.speak("Opening facebook.com")
            webbrowser.open("facebook.com")   
            nix.speak("Done for you! Anything else for me?")

        elif 'open twitter' in query:
            nix.speak("Opening twitter.com")
            webbrowser.open("twitter.com")   
            nix.speak("Done for you! Anything else for me?")

        elif 'play music' in query:
            nix.speak("Playing music from your music library")
            music_dir = 'D:\\Music'
            nix.songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            nix.speak("Done for you! Anything else for me?")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            nix.speak(f"Sir, the time is {strTime}")
            nix.speak("Done for you! Anything else for me?")

        elif 'open word' in query or 'open ms word' in query or 'ms word' in query:
            nix.speak("Opening Microsoft Office Word")
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(wordPath)
            nix.speak("Done for you! Anything else for me?")

        elif 'open code' in query:
            nix.speak("Opening Microsoft Visual Studio")
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Enterprise\\Common7\\IDE\devenv.exe"
            os.startfile(codePath)
            nix.speak("Done for you! Anything else for me?")

        elif 'whats up' in query:
            nix.speak('Just doing my thing')

        elif 'email to' in query or 'mail to' in query:
            receiver = query.split(" ")[len(query.split(" "))-1]
            to = email_nix.findReceiver(receiver)
            if to != 0:
                try:
                    nix.speak("What is your message?")
                    content = sr.takeCommand()
                    #to = ""
                    email_nix.sendEmail(to, content)
                    nix.speak("Email has been sent")
                    print("Email has been sent!")
                except Exception as e:
                    print(e)
                    nix.speak("Sorry Akash, something went wrong and I am not able to send your email right now.")
                    print("Sorry Akash, something went wrong and I am not able to send your email right now.")
            
        elif 'tell me a joke' in query:
            response = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
            if response.status_code == requests.codes.ok:
                nix.speak("Here is an awesome joke for you")
                nix.speak(str(response.json()['joke']))
            else:
                nix.speak("Oops! I ran out of jokes.")

        elif "calculate" in query:
            # WolframAlpha API ID 
            api_id = "4X6QVJ-A9WT8HV3XH" 
            client = wolframalpha.Client(api_id) 
  
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            nix.speak("The answer is " + answer)

        elif 'what is the weather status' in query or 'weather status' in query or 'weather' in query:
            weather_nix.weather()

        elif 'headlines' in query or 'news' in query or 'headline' in query:
            news_nix.givenews()

        elif 'covid-19' in query or 'corona' in query:
            covid19_nix.covid_19()
            nix.speak("Anything else for me?")

        elif 'how are you' in query:
           print("I am fine, what about you?")
           nix.speak("I am fine, what about you?")
        
        elif 'fine' in query:   
            print("Great")
            nix.speak("Great")

        elif 'awesome' in query or 'wow' in query or 'amazing' in query or 'wonderful' in query:
            print("Thank you sir, I am always here for you!")
            nix.speak("Thank you sir, I am always here for you!")

        elif 'thank you' in query or 'thanks' in query or 'thank you nix' in query:
            print("You are always welcome Akash!")
            nix.speak("You are always welcome Akash!")

        elif 'lock' in query or 'lock windows' in query:
            win_nix.lock()

        elif 'sign out my pc' in query or 'sign out my computer' in query:
            nix.speak("Confirm me by saying yes or no")
            print("Do you wish to sign out your computer? (Yes/No)")
            trigger = sr.takeCommand()
            if trigger == "yes":
                nix.speak("Your computer will sign out within 5 seconds, countdown will start now.")
                t = 5
                win_nix.logoff(int(t))
            else:
                print("Okay!")
                nix.speak("Okay, what's next?")

        elif 'restart my pc' in query or 'restart my computer' in query:
            nix.speak("Confirm me by saying yes or no")
            print("Do you wish to restart your computer? (Yes/No)")
            trigger = sr.takeCommand()
            if trigger == "yes":
                nix.speak("Your computer will restart within 5 seconds, countdown will start now.")
                t = 5
                win_nix.restart(int(t))
            else:
                print("Okay!")
                nix.speak("Okay, what's next?")

        elif 'turn off my pc' in query or 'shutdown my computer' in query:
            nix.speak("Confirm me by saying Yes or No")
            print("Do you wish to shutdown your computer? (Yes/No)")
            trigger = sr.takeCommand()
            if trigger == "yes":
                nix.speak("Your computer will shutdown within 5 seconds, countdown will start now.")
                t = 5
                win_nix.shutdown(int(t))
            else:
                print("Okay!")
                nix.speak("Okay, what's next?")

        elif 'bye' in query or 'quite' in query or 'exit' in query or 'close' in query or 'nope' in query:
            print("Thanks for using nix! See you later, bye!")
            nix.speak("Thanks for using nix! See you later, bye!")
            exit()

        else:
            nix.speak("I don\'t know what you mean! I can understand commands like open facebook, weather status, headlines and tell me a joke")
