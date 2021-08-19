<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">

<div style="text-align:center"><img src="https://raw.githubusercontent.com/d8rkmind/Pylookup/main/Pylookup.png"></div>
  
<h1>PyLookup</h1>

<p> an OSINT porject completly on python ,previously named <b>Profounder</b> 
  mainly to find given username in some website and to scrap urls from a diven website.
  still need to be improved 
<br></p>

<h2>Installation</h2>

```markdown
cd Pylookup
pip3 install -r requirements.txt
```
<b>Usage :</b>

```
python3 Pylookup.py [OPTIONS]
```
<h2>Command-line Usage Information</h2>
There are mainly 2 subcommands in the script 

Sub commands  | Functionality
------------- | -------------
find (-f)  | To search for an username in specific websites
 scrap (-s ) | To do url scrapping from a website
 
 Example :
 
 ```
 python3 Pylookup.py find
          or 
 python3 Pylookup.py scrap
 
 ```
 
<br> 
Giving the above options as argument it will spawn an interactive shell (I_S) to work on 
Typing help as input will show all the following inbuild commands to work on 

Prompt commands | Functionality
----------------|--------------
show | to show options
set  | to set values to inbuild variables
run  | to activate the program with given variables
clear| to clear screen 


The project is still under development and will be added with more feature <br>
Hoping for the best 

<h3>Update informations</h3>

<b> v1.0</b>: Rewritten the code completely ,Improved interface
