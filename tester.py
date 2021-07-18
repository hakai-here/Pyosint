import requests

def t(na):

    base_url ="https://"
    url = base_url + na 
    response=requests.get(url)
    
    if(response.status_code == 200):
         print("  found \u279c ",url)
         return(url)
       
         
    else:
         print("found \u279c not found ")
         return("Not found")
        

name=input("\n enter :: ")
k=t(name)
print(k)