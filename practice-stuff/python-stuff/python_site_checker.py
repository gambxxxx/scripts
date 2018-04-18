import urllib.request
from colorama import Fore
from colorama import Style


while True:
    
    if print(urllib.request.urlopen("http://allutomotive.com/").getcode()) == '200':
        print (f'Site is {Fore.RED}DOWN{Style.RESET_ALL}')
        break
    else:
        print (f'Site is {Fore.GREEN}UP{Style.RESET_ALL}')
        print (urllib.request.urlopen("http://allutomotive.com/").getcode())
