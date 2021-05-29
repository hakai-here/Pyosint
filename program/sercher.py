import requests

def git(na):
    base_url ="https://www.github.com/"
    url = base_url + na +"/"
    response=requests.get(url)

    
    if(response.status_code == 200):
         print("github found \u279c ",url,"\n")
         return(url)
         
    else:
         print(" github \u279c not found\n ")
         return("not found ")


def facebook(na):
    base_url ="https://www.facebook.com/"
    url = base_url + na +"/"
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("facebook found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print(" facebook \u279c Not found\n ")
         return("Not found  ")

def twitter(na):
    base_url ="https://www.twitter.com/"
    url = base_url + na +"/"
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Twitter found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("Twitter \u279c not found ")

def tryhackme(na):
    base_url ="https://tryhackme.com/p/"
    url = base_url + na +"/"
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("tryhackme found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("tryhackme \u279c not found \n")
         return("Not found")

def fhtb(na):
    base_url ="https://forum.hackthebox.eu/profile/"
    url = base_url + na +"/"
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("HTB found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("Forum HTB not found \n")
         return("Not found")

def youtube(na):
    base_url ="https://youtube.com/"
    url = base_url + na +"/"
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Youtube found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print(" Youtube \u279c not found\n ")
         return("Not found")

def soundcloud(na):
    base_url ="https://soundcloud.com/"
    url = base_url + na +"/"
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("SC found \u279c ",url)
         return(url)
       
         
    else:
         print("Soundcloud \u279c not found \n")
         return(" Not found")


def linktree(na):
    base_url ="https://linktr.ee/"
    url = base_url + na 
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Linktree found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print(" Linktree \u279c not found \n")
         return("Not found")

def myspace(na):
    base_url ='https://myspace.com/'
    url = base_url + na +'/'
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Myspace found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("Myspace \u279c not found \n")
         return("Not found")

def spotify(na):
    base_url ='https://open.spotify.com/user/'
    url = base_url + na
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Spotify found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("Spotify \u279c not found \n")
         return("Not found")
                
def trello(na):
    base_url ="https://trello.com/"
    url = base_url + na +"/activity"
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Trello found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("Trello \u279c not found \n")
         return("Not found")

def pornhub(na):
    base_url ="https://pornhub.com/users/"
    url = base_url + na 
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Pornhub found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("Pornhub \u279c not found \n")
         return("Not found")

def xvideos(na):
    base_url ="https://www.xvideos.com/profiles/"
    url = base_url + na 
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Xvideos found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("Xvideos \u279c not found \n")
         return("Not found")

def steam(na):
    base_url ="https://steamcommunity.com/id/"
    url = base_url + na +"/"
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("Steam id found \u279c ",url,"\n")
         return(url)
       
         
    else:
         print("Steam \u279c not found \n")
         return("Not found")
        
