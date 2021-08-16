
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import time 

def printer(x):
    j=input("\n Enter the filename to be saved :: ")
    file=j+".html"
    f=open(file,"w+")
    text=x.read()
    f.write(text.decode('utf-8'))
    print("done")

def txtprint(y):
    j=input("\n Enter the filename to be saved :: ")
    file=j+".txt"
    f=open(file,"w+")
    text=y.read()
    f.write(text.decode('utf-8'))

def sorc():

    time.sleep(1)
    

    i=input("\n Enter the url :: ")




    try:
        html = urlopen(i)
    except HTTPError as a:
        print("Cannot be extracted , Error �")
    except URLError as a:
        print("Server not found! ,\n\tCommon reason � \n\t1) url typed incorrectly \n\t2) Actually not exist")
    else:
       print("Select yout prefered choice \u2193")
       print("\n \t 1 \u279c print the code \n \t 2 \u279c Save to html file \n \t 3 \u279c Save to an txt file ")
       k=int(input("\n \t Enter your choice \u27A2   "))
       if(k == 1):
            print(html.read())
       elif(k == 2):
            print("\n \t ⚠ IF an error happens while creating the file please run the program and use 'print option' and manually copy the code ⚠ \n")
            time.sleep(2)
            printer(html)
       elif(k == 3):
            txtprint(html)
       else:
            print("\n \t Wrong input ")
