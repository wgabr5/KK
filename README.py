from requests import get
from colorama import *
from random import randint as ri

def main():
    print(f' {Fore.CYAN}[{Fore.GREEN}-{Fore.CYAN}]{Fore.MAGENTA}  How much times do you want to try and generate a random code?: {Fore.CYAN}')
    amount = int(input(f'   '))
    print(f' {Fore.CYAN}[{Fore.GREEN}-{Fore.CYAN}]{Fore.MAGENTA}  Do you also want to log invalid codes? [Y/N]: {Fore.CYAN}')
    logyon = str(input(f'   '))
    print(f'{Fore.RESET}')

    if logyon == 'y' or logyon == 'Y':
        logyon = True

    for i in range(int(amount)):
        id = ri(1000000000, 9999999999)
        url = f'https://us06web.zoom.us/j/7616891834?pwd=Z8tSjkGTVv0BdPMJ4ljutpszO0TspZ.1'

        r = get(url)

        if 'This meeting link is invalid' in str(r.content):
            print(f' {Fore.CYAN}[{Fore.GREEN}-{Fore.CYAN}]{Fore.MAGENTA}  Found the meeting {Fore.CYAN}{url}{Fore.MAGENTA}!{Fore.RESET}')

        else:
            if logyon == True:
                print(f'{Fore.RED} [-]  Invalid meeting: {url}{Fore.RESET}')

if __name__ == '__main__':
    init(convert=True)
    main()
