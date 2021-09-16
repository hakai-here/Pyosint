#!/usr/bin/python3

import argparse
import requests.exceptions 
from resources.agentk import run
from resources.webagent import run_main
from sys import argv as argu
import resources.enumsub as subdom
import os



G = '\033[92m'  
Y = '\033[93m'  
B = '\033[36m'  
R = '\033[91m' 
W = '\033[0m'
L = "\033[90m"

def parse_arg():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + argu[0] + " ")
    parser._optionals.title = "OPTIONS"
    parser.add_argument("-m",'--module',help="To specify the module to use ",required=True)
    parser.add_argument("-n",'--name' ,help="Username or domain name ",required=True)
    parser.add_argument("-o",'--output' ,help="Name  of the output file ",default=None)
    parser.add_argument("-t",'--threads',help="To set thread value ",type=int,default=50)
    parser.add_argument("-l",'--limit',help="To set the max limit for web crawling",default=30)
    parser.add_argument("-v","--verbose",help="To enable verbose",nargs='?',default=False)
    parser.add_argument("-p",'--ports',help="To set the ports for subdomain enum{seperate by using commas eg: 80,443}")
    return parser.parse_args()

#````````````````````````````````````````````````````````````````````````````````````````

#````````````````````````````````````````````````````````````````````````````````````````
def main():
    agrument = parse_arg()
    
    module=agrument.module
    name = agrument.name
    output = agrument.output
    thread = agrument.threads
    limit = agrument.limit
    port = agrument.ports
    verbose = agrument.verbose

    if (module == "find"):
        run(username=name,output=output,threads=thread)
    elif (module == "crawl" or module == "scrap" or module == "web"):
        run_main(x=name,max=limit,filename=output)
    elif  (module == "enum" or module == "sub-domain"):
            subdom.main(domain=name,threads=thread,savefile=output,ports=port,verbose=verbose)
    else:
        print(f"\n {R} Module not found ")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Y}Keybord interrupt found Exiting the program :) {W}")
        exit(0)
    except requests.exceptions.MissingSchema:
        print(f"{R}\n Missing schema. Perhaps you miss 'http://' ")
