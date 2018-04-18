import urllib.request
import time
from colorama import Fore
from colorama import Style

type(print(urllib.request.urlopen("http://allutomotive.com/").getcode()))
'''
def check_uptime():
    while True:
        up_time = print(urllib.request.urlopen("http://allutomotive.com/").getcode())
        if up_time != 200:
            print (f'Site is {Fore.RED}DOWN{Style.RESET_ALL}')
            break
        else:
            print (f'Site is {Fore.GREEN}UP{Style.RESET_ALL}')
            time.sleep(5)

check_uptime()
'''