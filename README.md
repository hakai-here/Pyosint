<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">
<p align="center">
<img src="https://raw.githubusercontent.com/d8rkmind/PyOsint/main/Pyosint.png"></p>
<h1>Pyosint</h1>
  

<p> An OSINT project entirely in python, previously referred to as Profounder, mainly to find user names given in specific websites and to remove URLs from a given website,Still in its development phase.
<br></p>

<h2>Installation</h2>

```markdown
cd PyOsint
pip3 install -r requirements.txt
```
<b>Usage :</b>

```
python3 Pyosint.py [OPTIONS]
```
<h2>Command Line Utilization Information.</h2>

There are mainly two sub-commands in the script 

Arguments |Shot<br>form    | Functionality
----------|-- | -------------
  find |-f    | To search for a user name from specific Web sites.
 scrap |-s   | For scrapping url from a website.
 enum  |-e   | to count the number of subdomains on a website(enumeration)
 
 
 ```
 python3 Pyosint.py find
 
 python3 Pyosint.py scrap
 
 python3 Pyosint.py enum
 ```
 
<br> 
By giving the above options as argument, it will generate an interactive shell which you can work with for the corresponding functions.
Entering the input "help" shows all of the following build commands.

Commands | Functionality
----------------|--------------
show | for displaying options.
set  | for defining values for the inbuild variables.
run  | for activating the program with specified variables.
clear| for erasing the screen.
help | to show help option in the module



The project is still in development and will be added with additional functionality.<br>Happy to hear suggestions for improvement.


<h3>Update informations</h3>

<h4> update-18-8-21</h4>:<br> 
Rewritten the code completely ,Improved interface
<br>
<h4> update-20-8-21</h4>: 
Added subdomain enumeration module(enum) modified version of [Sublist3r2](https://github.com/RoninNakomoto/Sublist3r2) 

 
 
