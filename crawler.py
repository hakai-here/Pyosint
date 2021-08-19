import collections
import requests
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import colorama
   #colors for diffrent modules
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW

internal_urls= set()
external_url= set()

def is_valid(url): #check if url is valid
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url): #return urls from a website
    
    urls=set() #urls
    domain_name=urlparse(url).netloc
    soup=BeautifulSoup(requests.get(url).content,"html.parser")
    for a_tag in soup.findAll("a"):
        href=a_tag.attrs.get("href")
        if href == ""or href is None:
            continue #empty tag

        href=urljoin(url,href)
        parsed_herf = urlparse(href)
        href= parsed_herf.scheme+"://"+parsed_herf.netloc+parsed_herf.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            if href not in external_url:
                print(f"{GRAY} [⎇] External link --> {href}{RESET}")
                external_url.add(href)
            continue
        print(f"{GREEN} [➤] Internal links --> {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls

total_url_visited = 0

def crawl(url,max_url=30):
    global total_url_visited
    total_url_visited+= 1
    print(f"{YELLOW} [Δ] Crawling --> {url}{RESET}")
    links=get_all_website_links(url)
    for link in links:
        if total_url_visited > max_url:
            break
        crawl(link,max_url=max_url)
def web(i,j):
    crawl(i,j)
    print("[\u297c] Total internal links:",len(internal_urls))
    print("[\u297c] Total External links:",len(external_url))
    print("[\u297c] Total Scrapped  Urls:",len(external_url)+len(internal_urls))
    
