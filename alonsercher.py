import os
import requests 
def alon():

    templat={"github":"https://www.github.com/","facebook":"https://www.facebook.com/","twitter":"https://www.twitter.com/","tryhackme":"https://tryhackme.com/p/","hackthebox":"https://forum.hackthebox.eu/profile/","youtube":"https://youtube.com/","soundcloud":"https://soundcloud.com/","linktree":"https://linktr.ee/","myspace":"https://myspace.com/","spotify":"https://open.spotify.com/user/","trello":"https://trello.com/","pornhub":"https://pornhub.com/users/","xvideos":"https://www.xvideos.com/profiles/","steam":"https://steamcommunity.com/id/"}
    print("\n please type the site you want to search for from the prebuild templates \n")

    os.system("cat ~/program/resources/lists.txt")
    i=input("Enter the site you want from above :")
    base_url=templat[i]
    j=input("\n Enter the user name you want to search \u279c ")
    url=base_url+j
    response=requests.get(url)

    if(response.status_code == 200):
         print("  found \u279c ",url)
    
    return
