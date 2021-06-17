#coding:UTF-8
from multiprocessing import Pool
import colorama
import requests
import re
import os
colorama.init()

m = "\033[36m"
b = "\033[0m"

wpdorks = ['("Just another WordPress site")','("Comment on Hello world!")','("Proudly powered by WordPress")','("Mr WordPress on Hello world!")']
opcdorks = ['index.php?route=']
jomdorks = ['com_user.','com_forum.']

def dorkscanner(dork):
      start = 0
      while start < 800:
        try:
          r = requests.get("http://www.bing.com/search?q="+dork+"&count=50&first="+str(start))
          find = re.findall('<h2><a href="(.*?)"', r.text)
          for xm in find:
              if "http://" in xm:
                  print(m+r"http://"+re.findall('http://(.*?)/',xm)[0]+"/")
                  open("sites.txt", "a+").write("http://"+re.findall('http://(.*?)/',xm)[0]+"/\n")
              elif "https://" in xm:
                  print(m+r"https://"+re.findall('https://(.*?)/',xm)[0]+"/")
                  open("sites.txt", "a+").write("https://"+re.findall('https://(.*?)/',xm)[0]+"/\n") 
          start = start + 20
        except:
             pass
def dorkmaker():
           print(m+"\n ["+b+" 1 "+m+"] WordPress") 
           print(m+" ["+b+" 2 "+m+"] OpenCart")
           print(m+" ["+b+" 3 "+m+"] Joomla")
           print(m+" ["+b+" 4 "+m+"] Menu\n")
           while True:
                 try:
                    ss = int(raw_input(m+" [ "+b+"+ "+m+u"] Seçiminiz : "+b))
                 except:
                      pass
                 if ss == 1:
                      dorks = []
                      word = raw_input(m+" [ "+b+"+ "+m+u"] Herhangi bir metin ekleyiniz : "+b)
                      words = word.split()
                      for i in wpdorks:
                          for x in words:
                             dorks.append(i+x)
                      print(m+" [ "+b+"+ "+m+u"] Oluşturulan dork sayısı : "+b+str(len(dorks)))
                      print(m+" [ "+b+"+ "+m+u"] Dorklar dorks.txt'ye kaydedildi!")
                      wri = open("dorks.txt","w")
                      for d in dorks:
                           wri.write(d+"\n")
                      exit()
                 elif ss == 2:
                      dorks = []
                      word = raw_input(m+" [ "+b+"+ "+m+u"] Herhangi bir metin ekleyiniz : "+b)
                      words = word.split()
                      for i in opcdorks:
                          for x in words:
                             dorks.append(i+x)
                      print(m+" [ "+b+"+ "+m+"] Oluşturulan dork sayısı : "+b+str(len(dorks)))
                      print(m+" [ "+b+"+ "+m+"] Dorklar dorks.txt'ye kaydedildi!")
                      wri = open("dorks.txt","w")
                      for d in dorks:
                           wri.write(d+"\n")
                      exit()
                 elif ss == 3:
                      dorks = []
                      word = raw_input(m+" [ "+b+"+ "+m+"] Herhangi bir metin ekleyiniz : "+b)
                      words = word.split()
                      for i in jomdorks:
                          for x in words:
                             dorks.append(i+x)
                      print(m+" [ "+b+"+ "+m+"] Oluşturulan dork sayısı : "+b+str(len(dorks)))
                      print(m+" [ "+b+"+ "+m+"] Dorklar dorks.txt'ye kaydedildi! ")
                      wri = open("dorks.txt","w")
                      for d in dorks:
                           wri.write(d+"\n")
                      exit()
                 elif ss == 4:
                      if os.name == "nt":
                          os.system("cls")
                      else:
                          os.system("clear")
                      banner()
                      break
              
def menu():
      print(m+"""
 ["""+b+""" 1 """+m+u"""] Dork Oluşturucu [WordPress,OpenCart,Joomla]
 ["""+b+""" 2 """+m+u"""] Bing kullanarak hızlı dork taraması
 ["""+b+""" 3 """+m+u"""] Çıkış
      """)

def banner():
      print(m+"""
                       d8b                d8,                d8b                                                 
                       ?88               `8P    d8P          ?88                            d8P                  
                        88b                  d888888P         88b                        d888888P                
 ?88   d8P  d8P d8888b  888888b  .d888b,  88b  ?88'   d8888b  888888b ?88   d8P  88bd88b   ?88'   d8888b  88bd88b
 d88  d8P' d8P'd8b_,dP  88P `?8b ?8b,     88P  88P   d8b_,dP  88P `?8bd88   88   88P' ?8b  88P   d8b_,dP  88P'  `
 ?8b ,88b ,88' 88b     d88,  d88   `?8b  d88   88b   88b     d88   88P?8(  d88  d88   88P  88b   88b     d88     
 `?888P'888P'  `?888P'd88'`?88P'`?888P' d88'   `?8b  `?888P'd88'   88b`?88P'?8bd88'   88b  `?8b  `?888P'd88'     
                                                                                                                 
                                                                                                                                                                              
 ["""+b+""" # """+m+"""] ElitHatZ AR-GE
 ["""+b+""" # """+m+"""] Kodlayan : Walker
 ["""+b+""" # """+m+u"""] İletişim : instagram.com/muso_yavuz
       """)

if __name__=="__main__":
   if os.name == "nt":
         os.system("cls")
   else:
         os.system("clear")
   banner()
   while True:
      menu()
      try:
          s = int(raw_input(m+" [ "+b+"+ "+m+u"] Seçiminiz : "+b))
      except:
         pass
      if s == 1:
           dorkmaker()
      elif s == 2:
           dorks = open(raw_input(m+" [ "+b+"+ "+m+"] Dork listesi : "+b),"r").read().splitlines()
           print("")
           p = Pool(15)
           p.map(dorkscanner, dorks)
           exit()
      elif s == 3:
           exit()
      else:
           pass