import os 
import time
import sys
import itertools
import threading
def s():
    if(os.name == 'posix'):
        os.system("clear")
    else:
        os.system("cls")
        
done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r\tDone!     ')
    time.sleep(1)

t = threading.Thread(target=animate)
t.start()
time.sleep(3)
done = True
        
        
        
