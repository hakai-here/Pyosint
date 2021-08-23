#!/usr/bin/python3

import os
import sys
import requests 
import subdomenum
from furrylamppylookup import fancy as fan
from furrylamppylookup import art 
from random import randint
from crawler import web as cralweb
from time import sleep 
from requests.exceptions import ConnectionError

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

def run_find(j):
    i=1
    k=1
    template={1:"https://www.github.com/",2:"https://www.facebook.com/",3:"https://www.twitter.com/",4:"https://tryhackme.com/p/",5:"https://forum.hackthebox.eu/profile/",6:"https://youtube.com/",7:"https://soundcloud.com/",8:"https://linktr.ee/",9:"https://myspace.com/",10:"https://open.spotify.com/user/",11:"https://trello.com/",12:"https://pornhub.com/users/",13:"https://www.xvideos.com/profiles/",14:"https://steamcommunity.com/id/",15:"https://www.npmjs.com/~",16:"https://www.7cups.com/@",17:"https://about.me/",18:"https://independent.academia.edu/",19:"https://discussions.apple.com/profile/",20:"https://ask.fm/",21:"https://audiojungle.net/user/",22:"https://blip.fm/",23:"https://www.bandcamp.com/",24:"https://bitbucket.org/",25:"https://bodyspace.bodybuilding.com/",26:"https://www.bookcrossing.com/mybookshelf/",27:"https://www.cnet.com/profiles/",28:"https://career.habr.com/",29:"https://www.cloob.com/name/",30:"https://community.cloudflare.com/u/",31:"https://www.codecademy.com/profiles/",32:"https://www.codechef.com/users/",33:"https://www.colourlovers.com/lover/",34:"https://www.cloob.com/name/",35:"https://www.colourlovers.com/lover/",36:"https://www.dailymotion.com/",37:"https://www.designspiration.net/",38:"https://www.discogs.com/user/",39:"https://disqus.com/",40:"https://hub.docker.com/u/",41:"https://dribbble.com/",42:"https://www.duolingo.com/profile/",43:"https://ello.co/",44:"https://euw.op.gg/summoner/userName=",45:"https://www.eyeem.com/u/",46:"https://f3.cool/",47:"https://facenama.com/",48:"https://www.flickr.com/people/",49:"https://my.flightradar24.com/",50:"https://flipboard.com/@",51:"https://fortnitetracker.com/profile/all/",52:"https://www.freelancer.com/u/",53:"https://freesound.org/people/",54:"https://giphy.com/",54:"https://gitlab.com/",55:"https://gitee.com/",56:"https://www.goodreads.com/",57:"http://en.gravatar.com/",58:"https://gurushots.com/",59:"https://hackaday.io/",60:"https://news.ycombinator.com/user?id=",61:"https://hackerone.com/",62:"https://hackerrank.com/",63:"https://www.house-mixes.com/profile/",64:"https://houzz.com/user/",65:"https://imgur.com/user/",66:"https://www.instructables.com/member/",67:"https://issuu.com/",68:"https://itch.io/profile/",69:"https://www.kongregate.com/accounts/",70:"https://launchpad.net/~",71:"https://leetcode.com/",72:"https://letterboxd.com/",73:"https://lichess.org/@/",74:"https://lolchess.gg/profile/na/",75:"https://www.memrise.com/user/",76:"https://www.mixcloud.com/",77:"https://myanimelist.net/profile/",78:"https://blog.naver.com/",79:"https://www.openstreetmap.org/user/",80:"https://opensource.com/users/",81:"https://otzovik.com/profile/",82:"https://forums.pcgamer.com/members/?username=",83:"https://psnprofiles.com/",84:"https://pastebin.com/u/",85:"https://www.patreon.com/",86:"https://www.periscope.tv/",87:"https://www.pinterest.com/",88:"https://pokemonshowdown.com/users/",89:"https://www.producthunt.com/@",90:"http://promodj.com/",91:"https://pypi.org/user/",92:"https://quizlet.com/",93:"https://www.quora.com/profile/",94:"https://raidforums.com/User-",95:"https://rateyourmusic.com/~",96:"https://www.redbubble.com/people/",97:"https://www.reddit.com/user/",98:"https://repl.it/@",99:"https://www.reverbnation.com/",100:"https://www.roblox.com/user.aspx?username=",101:"https://scratch.mit.edu/users/",102:"https://www.scribd.com/",103:"https://pikabu.ru/@",104:"https://osu.ppy.sh/users/",105:"https://www.npmjs.com/~",106:"https://note.com/",107:"https://www.nn.ru/",108:"https://www.nairaland.com/",109:"https://moikrug.ru/",110:"https://www.mercadolivre.com.br/perfil/",111:"https://mastodon.social/@",112:"https://forum.leasehackr.com/u/",113:"https://last.fm/user/",115:"https://kwork.ru/user/",116:"http://www.jeuxvideo.com/profil/",117:"https://www.interpals.net/",118:"https://www.hackster.io/",119:"https://www.geocaching.com/p/default.aspx?u=",120:"https://www.fl.ru/users/",121:"https://www.fixya.com/users/",122:"https://www.drive2.ru/users/",123:"https://www.babyblog.ru/user/info/",124:"http://www.authorstream.com/",125:"https://aminoapps.com/u/",126:"https://www.zhihu.com/people/",127:"https://youpic.com/photographer/",128:"https://www.younow.com/",129:"https://xboxgamertag.com/search/",130:"https://profiles.wordpress.org/",131:"https://community.windy.com/user/",132:"http://www.wikidot.com/user:info/",133:"https://weheartit.com/",134:"https://vimeo.com/",135:"https://vero.co/",136:"https://unsplash.com/@",137:"https://ultimate-guitar.com/u/",138:"https://data.typeracer.com/pit/profile?user=",139:"https://www.trakt.tv/users/",140:"https://www.tradingview.com/u/",141:"https://ch.tetr.io/u/",142:"https://steamcommunity.com/groups/",143:"https://scratch.mit.edu/users/",144:"https://www.scribd.com/",145:"https://slashdot.org/~",146:"https://slideshare.net/",147:"https://www.smule.com/",148:"https://sourceforge.net/u/",149:"https://www.sparkpeople.com/mypage.asp?id="}
    for i in range (1,150):
        if(i == 107 or i == 114):
            i+=1
        base_url=template[i]
        url=base_url+j    
        try:
            response=requests.get(url)
            if (response.status_code == 200):
                print(" ╬➤ "+ url)
                print(" ╬")
            else:
                pass
        except ConnectionError:
            print(" ╬")
            print(" ╬➤ [DEBUG] Connection timed out .sleeping for 1 sec")
            print(" ╬")
            sleep(1)
            i+=1

    
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
            initv=fan(3,24,3,col,"Find ")
            k = mine
            inlist = initv.split()
            if (inlist[0] == "help"):
                print(''' \n
                
                 You can run following commands:

                    help  - To display help menu 
                    clear - To clear screen
                    set   - To specify a value for username.

                            set username <name>
                        
                            
                            If you wish to remove the banner type : \033[1m set banner off \033[0m  
                            and clear the screen
                        
                   
                    To search at all the above sites at same time \033[1m set site all \033[0m


                    show  - to show the set options
                    run   - to execute the program 
                
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
                
                print("\n"+fan(2,1,50)+"\n")
            
            elif(inlist[0] == "run"):
                run_find(username)


            elif(inlist[0] == "set"):
                col = 0
                if(inlist[1] == "username" or inlist[1] == "name"):
                    username = inlist[2]
                elif(inlist[1] == "banner"):
                    if(inlist[2] == "off"):
                        mine=0
                    elif(inlist[2] == "on"):
                        mine=randint(1,7)


            else:
                print ("\n Wrong input try again : \n")
                col=1
    elif (argument == "-e" or argument=="enum"):
        subdomenum.callin()

    elif(argument == "-s" or argument=="scrap"):
        art(k)
        initliz()
        repetvalue = 1
        col =0
        mine = k
        while repetvalue == 1:
            initv=fan(3,24,3,col,"Scrap ")
            k = mine
            inlist = initv.split()
            if (inlist[0] == "help"): # to be added services 
                print(''' \n    
                
                 You can run following commands:

                    help  - To show help menu 
                    clear - To clear screen
                    set   - To specify a value for different variables.

                            set domain <domain/webpage>
                            set service <http/https> 

                            If you wish to remove the banner type : \033[1m set banner off \033[0m  
                            and clear the screen

                    show -> show options 
                    run  -> to execute the program
                
                
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
            
            elif(inlist[0] == "scrap" or inlist[0]=="run"):
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
