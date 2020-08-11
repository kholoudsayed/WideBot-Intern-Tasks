# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vVBCp4yp0rVLurKcrNzwVlvEsE5i-lTT

# ***Imports and Constants***
"""

from bs4 import BeautifulSoup
import time
import requests

RANDOM_PATH = "https://en.wikipedia.org/wiki/Special:Random"
TARGET_PATH = 'https://en.wikipedia.org//wiki/Philosophy'
MAX_ITR = 50
URLS_VISITED = [RANDOM_PATH]

"""## ***Search for Links***

As shown in Geting philosphy We need to get link in *[Clicking on the first link in the main text of a Wikipedia article ] *

Main Text ---> found in the div class="mw-content-text" .

search link in this Main Text -->Frist Link in div

ID="mw-content-text" Contain :

div class= mw-parser-output --->GET frist Link

noScript

div = printfooter
"""

def Fetch_Link(All_para):
  for i in All_para:
    if i.find("a"):
            Link_Found = i.find("a")
            Url  =Link_Found.get('href')
            break
    
  if Url is None : 
    return
  else :
    return  Url

def Search(link):
  #Conditions to Stop :
  #1- reach to 50 itiration 
  #2- Link not found --->WE Can Check it here
  #3 - Reach to philosphy
  #4- if one Link  repeated --> will Enter in finite loop

  Main_Text = requests.get(link).text  # Get ALl Content 

  soup = BeautifulSoup(Main_Text,"html.parser") 
  # Content  Div 
  content_text_Div = soup.find(id="mw-content-text")  
  # Get Frist Class
  parser_output_Div = content_text_Div.find(class_ = 'mw-parser-output')  
  # list of Paraph in class mw-parser-output
  List_Of_Paragraph = parser_output_Div.find_all("p")  

  Url = Fetch_Link(List_Of_Paragraph)

  if (Url is None):
    return
 
  Complete_Link = 'https://en.wikipedia.org/'+ Url
  
  return Complete_Link

'''
a=Search('https://en.wikipedia.org//wiki/Greek_language')
a
'''

"""# ***Consitions***"""

#condition to continue :
#len of itirstions or length Visited URL < MaxITR
#Final link not in Visited URL
#Target Link (Philosphi) != any Link in Visited URL


def Conditions(URLS_VISITED):
  cond1 = len(URLS_VISITED) > MAX_ITR
  cond2 = URLS_VISITED[len(URLS_VISITED)-1]  in URLS_VISITED[:(len(URLS_VISITED)-1)]
  cond3 = (TARGET_PATH == URLS_VISITED[len(URLS_VISITED)-1])
  print(cond1)
  print(cond2)
  print(cond3)




  if (cond1):
  
    print("not satisfied conditions")
    print("crossed limits of iterations ")
    return False
  elif (cond2):
    print("not satisfied conditions")
    print("Final link  in Visited URL")
    return False 

  elif (cond3):
    print(" satisfied conditions")
    print("Target Link (Philosphi) you reach ,Congratulations!! ")
    print("Done ")

    return False 

  else :
    return True

while Conditions(URLS_VISITED):
    link = Search(URLS_VISITED[len(URLS_VISITED)-1])
    if not link:
        print("No Links in This Page.")
        break
    URLS_VISITED.append(link)

URLS_VISITED

"""Get No link 
  
  'https://en.wikipedia.org//wiki/Greek_language'

  'https://en.wikipedia.org//wiki/Country

  Repeated link

   'https://en.wikipedia.org//wiki/International_Phonetic_Alphabet'

  'https://en.wikipedia.org//wiki/Science'

  Need to repeate Runs to Reach to Philosophy
"""