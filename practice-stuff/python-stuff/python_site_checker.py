import urllib.request
import time
from colorama import Fore
from colorama import Style


def check_uptime():
    while True:
        
        if print(urllib.request.urlopen("http://allutomotive.com/").getcode()) == '200':
            print (f'Site is {Fore.RED}DOWN{Style.RESET_ALL}')
            break
        else:
            print (f'Site is {Fore.GREEN}UP{Style.RESET_ALL}')
            print (urllib.request.urlopen("http://allutomotive.com/").getcode())
            time.sleep(5)

check_uptime()
