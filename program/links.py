
def changer(x):
    x=x.strip()
    x=x.replace(" ","%20")
    return(x)

def blink(x):
    url="https://www.bing.com/search?q="+x+"&go=&form=QBLH&filt=all"
    return(url)

def glink(x):
    url="https://www.google.com/search?q="+x+"&num=30"
    return(url)

def duck(x):
    url="https://duckduckgo.com/lite/?q="+x
    return(url)




