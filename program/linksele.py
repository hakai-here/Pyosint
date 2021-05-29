import links
def selector(y,link):
    if(y == "bing"):
        k=links.blink(link)
        return(k)
    elif(y =="google"):
        k=links.glink(link)
        return(k)
    elif(y == "duckduckgo"):
        k=links.duck(link)
        return(k)