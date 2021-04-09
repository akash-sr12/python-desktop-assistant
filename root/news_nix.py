# (c) 2020 - Akash Sarkar
# news_nix

import sys
sys.path.insert(0, 'E:/Projects/Python/myAssistant/nixAssistant/root/common/')

import requests, json

import speak_nix as nix

def givenews():
    apiKey = "85d1024e0ceb4dae849c4783ad8753a4"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 10:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            nix.speak("Today's top ten Headline are : ")
            flag = False
        else:
            nix.speak("Next news :")
        nix.speak(to_speak)
