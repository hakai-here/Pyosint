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
    elif (module == "crawl" or module == "scrap"):
        run_main(x=name,max=limit)
    elif  (module == "enum" or module == "sub-domain"):
            subdom.main(domain=name,threads=thread,savefile=output,ports=port,verbose=verbose)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Y}Keybord interrupt found Exiting the program :) {W}")
        exit(0)
    except requests.exceptions.MissingSchema:
        print(f"{R}\n Missing schema. Perhaps you miss 'http://' ")

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
