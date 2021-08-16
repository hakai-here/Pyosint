import osinter
import os
from time import sleep
import alonsercher
import socodex
import linkes
import crawler


def s():
    if(os.name == 'posix'):
        os.system("clear")
    else:
        os.system("cls")

s()


askusr='y'
while(askusr == 'y' or askusr == 'Y'):
   
   print("The output from this program may vary from the one you are looking for  ")
   
   s()
   os.system("cat resources/logo.txt")#changes to be made
   os.system("cat resources/devinfo.txt")#changes to be made
   
   print("\n\n\t0 to exit \n\t1 search username on  all prebuild templates \n\t2 search username from a specific from prebuild template \n\t3 source code extractor  \n\t5 Web scrapping ")
   m=int(input("\n enter your choice \u279c "))
   if(m == 1):
       osinter.mainer()
   elif(m == 2):
      alonsercher.alon()
   elif(m == 3):
      socodex.sorc()
   elif(m == 4):
      linkes.act()
   elif(m==0):
      exit(0)
   elif(m == 5):
      crawler.web()

   
   askusr=input("Continue y/n ? ")
   if(askusr == "y" or askusr == "Y"):
      print("\n\n\tWarning \u279c all the information above on screen will be erased if it is not saved ")
      sleep(2)
      l=input(" Press enter to continue  ")
   else:
      print("\n\n\t Ok Bye :) ")
      exit(0)
   
    




