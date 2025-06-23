import time
from colorama import Fore, Style, init
init(autoreset=True)

name = input("What is your name? ")

print(Fore.LIGHTBLACK_EX + "\n{static crackle....}" + Style.RESET_ALL)
time.sleep(1)

print(Fore.RED + f"System override detected... Welcom {name}." + Style.RESET_ALL)
time.sleep(2)

print(Fore.RED + "\nYou shouldn't be here...")
time.sleep(2)

print(Fore.RED + "\nBut it's to late now." + Style.RESET_ALL)
time.sleep(1)

print(Fore.LIGHTBLACK_EX + "\n[connection sealed]" + Style.RESET_ALL)