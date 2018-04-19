import urllib.request
import time
from colorama import Fore
from colorama import Style

def check_uptime():
    while True:
        try:
            print(urllib.request.urlopen("http://localhost:7070/").getcode())
            print (f'Site is {Fore.GREEN}UP{Style.RESET_ALL}')
        except:
            print (f'Site is {Fore.RED}DOWN{Style.RESET_ALL}')
        #if print(urllib.request.urlopen("http://localhost:7070/").getcode()) == '200':
           # print (f'Site is {Fore.RED}DOWN{Style.RESET_ALL}')
            #break
        finally:
            #print (f'Site is {Fore.GREEN}UP{Style.RESET_ALL}')
            #print (urllib.request.urlopen("http://localhost:7070/").getcode())
            time.sleep(5)

check_uptime()
