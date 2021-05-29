import sercher
import os
from time import sleep

def screen_clear():
   if os.name == 'posix':
       _ = os.system('clear')
   else:
      _ = os.system('cls')

   print("The output from this program may vary from the one you are looking for  ")
   sleep(1)



screen_clear()

#os.system("cat logo.txt")
print("\n")

def mainer():
   name= input(" Enter the user to be searched : ")
   j=input("\n Enter the filename to be saved :: ")
   file=open(j+".txt","a")
   t="Top search results with ",name," as  username\n\n"
   file.write("".join(t))
   
   k=sercher.git(name)
   k="github \u279c "+k
   file.write("".join(k))
   file.write("\n\n")
   
   k=sercher.facebook(name)
   k="facebook \u279c "+k
   file.write("".join(k))
   file.write("\n\n")

   k=sercher.fhtb(name)
   k="forum_hackthebox \u279c "+k
   file.write("".join(k))
   file.write("\n")

   k=sercher.youtube(name)
   k="Youtube \u279c "+k
   file.write("".join(k))
   file.write("\n\n")

   k=sercher.soundcloud(name)
   k="SoundCloud \u279c "+k
   file.write("".join(k))
   file.write("\n\n")

   k=sercher.tryhackme(name)
   k="Tryhackme \u279c "+k
   file.write("".join(k))
   file.write("\n\n")
   
   k=sercher.linktree(name)
   k="Linktree \u279c "+k
   file.write("".join(k))
   file.write("\n\n")

   k=sercher.myspace(name)
   k="Myspace \u279c "+k
   file.write("".join(k))
   file.write("\n\n")

   k=sercher.spotify(name)
   k="Spotify \u279c "+k
   file.write("".join(k))
   file.write("\n")
   k=sercher.trello(name)
   k="Trello \u279c "+k
   file.write("".join(k))
   file.write("\n\n")
   
   k=sercher.pornhub(name)
   k="pornhub \u279c "+k
   file.write("".join(k),)
   file.write("\n\n")
   
   k=sercher.xvideos(name)
   k="pornhub \u279c "+k
   file.write("".join(k),)
   file.write("\n\n")
   
   k=sercher.steam(name)
   k="Steam community \u279c "+k
   file.write("".join(k),)
   file.write("\n\n")
   
   k=sercher.twitter(name)
   k="twitter \u279c "+k
   file.write("".join(k),)
   file.write("\n\n")

