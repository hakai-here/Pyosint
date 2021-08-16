import requests
import os
from urllib.request import urlopen
from urllib.error import HTTPError
import links
import linksele

def act():
   
    i=input("\n enter the request here :-->")
    i=links.changer(i)
    os.system("cat resources/linklist.txt") #changes should be made 
    j=input("\n Enter the browser of choice : ")
    j=j.lower()
    i=linksele.selector(j,i)
    response=requests.get(i)
    print(response," queue avaliable")
    if(response.status_code == 200):
        try:
            page=urlopen(i)
        except HTTPError as e:
            print("\n Error 403 -> forbidden access")
        else:
            html=page.read()
            k=input("Enter the name of the file (specify html/txt): ")
            f=open(k,"w")
            f.write(html.decode('utf-8'))
            f.write("\n")

    
