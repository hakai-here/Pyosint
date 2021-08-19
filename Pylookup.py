import os
import sys
import requests 
from furrylamppylookup import fancy as fan
from furrylamppylookup import art 
from random import randint
from crawler import web as cralweb

def clean():
    if(os.name == 'posix'):
        os.system("clear")
    else:
        os.system("cls")

def clear(x):
    clean()
    art(x)
    return 0

def crawljoin(x,y,z=30):
    k=y+"://"+x
    cralweb(k,z)

def initliz():
    print('''
    
        Type "help" to see options

     ''')

def url_f(x):
    response=requests.get(x)
    if(response.status_code == 200):
         print("  found  "+fan(2,77)+" "+x+" "+fan(2,62))

def run_find(sitw,j):
    template={1:"https://www.github.com/",2:"https://www.facebook.com/",3:"https://www.twitter.com/",4:"https://tryhackme.com/p/",5:"https://forum.hackthebox.eu/profile/",6:"https://youtube.com/",7:"https://soundcloud.com/",8:"https://linktr.ee/",9:"https://myspace.com/",10:"https://open.spotify.com/user/",11:"https://trello.com/",12:"https://pornhub.com/users/",13:"https://www.xvideos.com/profiles/",14:"https://steamcommunity.com/id/"}
    template2={'github':1,'facebook':2,'twitter':3,'tryhackme':4,'hbt-forum':5,'youtube':6,'soundcloud':7,'linktr':8,'myspace':9,'spotify':10,'trello':11,'pornhub':12,'xvideos':13,'steam':14}
    if(sitw == "all"):
        for i in range (1,15):
            base_url=template[i]
            url=base_url+j
            url_f(url)
    else:
        base=template2[sitw]
        base_url=template[base]
        url=base_url+j
        url_f(url)

    
def exiter():
    col = 0
    m=fan(3,24,2,2)
    if(m == "yes" or m == "Y" or m == "y" or m == "sure"):
        print("\nBye")
        sys.exit()
    
    else:
        d=input("\n Continue :) ")
        clear(k)
    
    return col

def main():
    username = "example"
    site = "all"
    weblink = "example.com"
    serv = "https"
    value = 30

    clean()
    k=randint(1,7)
    argument = sys.argv[1]


    if(argument == "-h" or sys.argv[1] == "help"):
        art(2)
        print(''' \n 
        Syntax as follows 
                
            python3 Pylookup.py [OPTIONS]

            Options :
                
               -f or find  --  To search for username 
               -s or scrap --  To scrap url from given website 

            example :
             python3 Pylookup.py find

         ''')

    elif(argument == "-f" or argument=="find"):
        art(k)
        initliz()
        mine = k
        repetvalue = 1
        col =0
        while repetvalue == 1:
            initv=fan(3,24,3,col)
            k = mine
            inlist = initv.split()
            if (inlist[0] == "help"):
                print(''' \n
                
                 You can run following commands:

                    help  - To show help menu 
                    clear - To clear screen
                    set   - To set a value of diffrent variables

                            set username <name>
                            set site <site-name>
                            
                            if You want to remove baner type \033[1m set banner off \033[0m  
                            and clear the screen
                        
                        These are the sites avaliable :

                        github  
                        facebook  
                        twitter  
                        tryhackme  
                        hbt-forum 
                        youtube  
                        soundcloud  
                        linktr  
                        myspace  
                        spotify  
                        trello  
                        pornhub  
                        xvideos  
                        steam 

                    To search at all the above sites at same time \033[1m set site all \033[0m


                    show  - to show the set options
                    run   - to execute the program with set options 
                
                 ''')
            elif (inlist[0]=="clear"):
                col = clear(k)
                
            
            elif (inlist[0]== "exit"):
                col=exiter()

            elif(inlist[0] == "show"):
                col =0
                print("\n Option       Value   ")
                print(fan(2,8,50))
                print("                       ")
                print(" Username  :   {}     ".format(username))
                print("                       ")
                print(" Sites     :   {}     ".format(site))
                print("\n"+fan(2,1,50)+"\n")
            
            elif(inlist[0] == "run"):
                run_find(site,username)


            elif(inlist[0] == "set"):
                col = 0
                if(inlist[1] == "username" or inlist[1] == "name"):
                    username = inlist[2]
                elif(inlist[1] =="site" or inlist[1] == "url"):
                    site = inlist[2]
                elif(inlist[1] == "banner"):
                    if(inlist[2] == "off"):
                        mine=0
                    elif(inlist[2] == "on"):
                        mine=randint(1,7)


            else:
                print ("\n Wrong input try again : \n")
                col=1
    
    elif(argument == "-s" or argument=="scrap"):
        art(k)
        initliz()
        repetvalue = 1
        col =0
        mine = k
        while repetvalue == 1:
            initv=fan(3,24,3,col)
            k = mine
            inlist = initv.split()
            if (inlist[0] == "help"): # to be added services 
                print(''' \n    
                
                 You can run following commands:

                    help  - To show help menu 
                    clear - To clear screen
                    set   - To set a value of diffrent variables

                            set domain <domain/webpage>
                            set service <http/https> 

                        if You want to remove baner type \033[1m set banner off \033[0m  
                        and clear the screen

                    show -> show options        
                
                
                 ''')
            elif (inlist[0]=="clear"):
                col=clear(k)
                
            
            elif (inlist[0]== "exit"):
                col = exiter()
                


            elif(inlist[0] == "show"):
                col =0
                print("\n Option       Value   ")
                print(fan(2,81,50))
                print("\n")
                print(" url      :   {}     ".format(weblink))
                print("\n")
                print(" service  :   {}     ".format(serv))
                print("\n")
                print(" Number   :   {}     ".format(value))
                print("\n"+fan(2,81,50)+"\n")
            
            elif(inlist[0] == "scrap"):
                crawljoin(weblink,serv)



            elif(inlist[0] == "set"):
                col = 0
                if(inlist[1] == "web" or inlist[1] == "url"):
                    weblink = inlist[2]
                elif(inlist[1] =="service" or inlist[1] == "url"):
                    serv = inlist[2]
                elif(inlist[1] =="value" or inlist[1] == "number"):
                    value  = inlist[2]

                elif(inlist[1] == "banner"):
                    if(inlist[2] == "off"):
                        mine=0
                    elif(inlist[2] == "on"):
                        mine=randint(1,7)
                else:
                    print ("\n Wrong input try again :\n")
                    col=1



            else:
                print ("\n Wrong input try again :")
                col=1

    
if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      print("\n Keybord interrupt , Exiting the program bye") 
      sys.exit()
