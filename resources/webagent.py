#!/usr/bin/python3

from urllib.parse import urljoin,urlparse
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from socket import gethostbyname
from time import sleep
from os import linesep
import requests



HEADERS = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language' : 'en-US,en;q=0.5',
           'Accept-Encoding' : 'gzip, deflate',
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/93.0.4577.63 Safari/537.36"
          }

ipaddr=[""]
spacer=[" ","External urls:"," "," "]
internalurl=set()
externalurl=set()
total_url_visited = 0

G = '\033[92m'  
Y = '\033[93m'  
B = '\033[36m'  
R = '\033[91m' 
W = '\033[0m'
L = "\033[90m"

def namer():
    name = "output/web/{name}.txt".format(name=ipaddr[1])
    return name

def write_file():
    name = namer()
    print(f"\n Writing Collected data to a file -> ' {name} ' : \n\n")
    
    with open (name,'a') as f:
        f.write("\n Internal Urls :"+ linesep*3)
        for i in internalurl:
            f.write(i + linesep)
        for i in spacer:
            f.write(i + linesep)
        for i in externalurl:
            f.write(i+linesep)
    print(f"[*] Total Numbers of internal url {len(internalurl)}")
    print(f"[*] Total Numbers of external url {len(externalurl)}")
    print(f"[*] Total Numbers of collected url {len(internalurl)+len(externalurl)}")

def indicator(x):
        k = urlparse(x).netloc
        list1=[]
        list2=[]
        searchlist=["Date","Server","Content-Type","Cache-Control","X-TEC-API-VERSION","X-TEC-API-ROOT","X-TEC-API-ORIGIN","Transfer-Encoding","Pragma"]
        headerlist=["X-Frame-Options","Content-Security-Policy","X-XSS-Protection","X-Content-Type-Options","Strict-Transport-Security","P3P","X-Powered-By","X-Download-Options","Content-Disposition","Public-Key-Pins","Expect-CT","Cross-Origin-Resource-Policy","Cross-Origin-Opener-Policy","Access-Control-Allow-Origin","Access-Control-Allow-Credentials","Cross-Origin-Embedder-Policy","Feature-Policy","X-DNS-Prefetch-Control","Referrer-Policy","X-Permitted-Cross-Domain-Policies"]
        try:
            response=requests.get(x,params=None, headers=HEADERS, cookies=None, auth=None, timeout=60).headers
        except requests.exceptions.ConnectionError:
            print("\n Unable to connect ")
            return

        ip = gethostbyname(k)
        ipaddr.append(str(ip))
        t = PrettyTable(["Raw Headers"," informations"])
        t.add_row([B+"IP",ip+W])
        for i in searchlist:
            if i in response:
                t.add_row([B+i,response[i]+W])
        print(t)

        for i in headerlist:
            if i in response:
                list1.append(i)

            else:
                list2.append(i)
        
        t = PrettyTable(['Headers', 'status'])
        for i in list1:
            k = G+i+W
            t.add_row([k,G+'✔'+W])

        for i in list2:
            k = R+i+W
            t.add_row([k,R+'✘'+W])

        print(t)



def valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def web_links(url):
    urls=set()
    domain_name=urlparse(url).netloc
    try:
        soup=BeautifulSoup(requests.get(url,headers=HEADERS).content,"html.parser")
    except requests.exceptions.ConnectionError:
        print(f'''{R}\n[-] Connection Error
             Not alowing for further connection to {url}
             Probably secure site with passwords
             Exiting Bye {W}''')
        write_file()
        exit(0)
        

    for a_tag in soup.findAll("a"):
        href=a_tag.attrs.get("href")
        if href == "" or href is None:
            continue

        href=urljoin(url,href)
        parsed_herf=urlparse(href)
        href= parsed_herf.scheme+"://"+parsed_herf.netloc+parsed_herf.path
        if not valid(href):
            continue
        if href in internalurl:
            continue
        if domain_name not in href:
            if href not in externalurl:
                print(f"{L}[-] External Link : {href}")
                externalurl.add(href)
            continue
        
        print(f"{G}[+] Internal Links : {href}")
        urls.add(href)
        internalurl.add(href)
    return urls

def crawl(url,max_url=50): 
    global total_url_visited
    total_url_visited+=1
    print(f"{B}[>] Now Crawling : {url}")
    links= web_links(url)
    for link in links:
        if total_url_visited > max_url:
            break
        crawl(link,max_url=max_url)

def run_main(x,max=50,filename=0):
    print(f"{G}\r\n Intial Header check in Website : \n {W}")
    indicator(x=x)
    print(f"{G}\n Starting the module Crawl{W}\n")
    crawl(x,max_url=max)
    write_file()
    


