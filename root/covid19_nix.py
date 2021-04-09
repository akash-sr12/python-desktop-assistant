# (c) 2020 - Akash Sarkar
# covid19_nix

import sys
sys.path.insert(0, 'E:/Projects/Python/myAssistant/nixAssistant/root/common/')

import os
import requests
import numpy as np 
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup 
from tabulate import tabulate

import speak_nix as nix

def covid_19():
    print("We are getting details from www.mohfw.gov.in")
    nix.speak("We are getting details from www.mohfw.gov.in")
    print("Please wait...")
    nix.speak("Please wait...")
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
    URL = 'https://www.mohfw.gov.in/'
  
    SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed','Foreign-Confirmed','Cured','Death'] 
  
    response = requests.get(URL).content 
    soup = BeautifulSoup(response, 'html.parser') 
    header = extract_contents(soup.tr.find_all('th')) 
  
    stats = [] 
    all_rows = soup.find_all('tr') 
  
    for row in all_rows: 
        stat = extract_contents(row.find_all('td')) 
        if stat: 
            if len(stat) == 5: 
                # last row 
                stat = ['', *stat] 
                stats.append(stat) 
            elif len(stat) == 6: 
                stats.append(stat) 
  
    stats[-1][1] = "Total Cases"
  
    stats.remove(stats[-1])
    objects = [] 
    for row in stats : 
        objects.append(row[1])  
  
    y_pos = np.arange(len(objects)) 
  
    performance = [] 
    for row in stats :
        try:
            performance.append(int(row[2]) + int(row[3]))

        except:
            print("")
            os.system('cls')
  
    table = tabulate(stats, headers=SHORT_HEADERS) 
    print(table)
    nix.speak("The result is on your screen.")
