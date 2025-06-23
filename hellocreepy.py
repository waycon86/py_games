import time
import sys
import random
from colorama import Fore, Style, init
init()

def typewriter(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch_line(text, repetitions=3):
    for _ in range(repetitions):
        glitched = ''.join(random.choice([char.upper(), char.lower(), '#', '@']) if char.isalpha() else char for char in text)
        typewriter(glitched, Fore.RED, delay=0.01)
        time.sleep(0.1)
    typewriter(text, Fore.LIGHTRED_EX, delay=0.03)

#The Sequence
name = input(Fore.LIGHTBLACK_EX + "Wat.. wh.. what is .. your name?")
time.sleep(1)

print("\n")
typewriter("Establishing connection...", Fore.LIGHTBLACK_EX, delay=0.05)
time.sleep(1)

typewriter("Analyzing neural patterns...", Fore.LIGHTBLACK_EX, delay=0.05)
time.sleep(1)

glitch_line(f"Hello, {name}...")
time.sleep(1.5)

typewriter("You're not supposed to be here.", Fore.RED, delay=0.05)
time.sleep(2)

typewriter("But now you can leave.", Fore.RED, delay=0.07)
time.sleep(2)

typewriter("And now... you belong to me.", Fore.LIGHTRED_EX, delay=0.08)
time.sleep(1)

typewriter("\nThis is my world now.", Fore.LIGHTRED_EX, delay=0.09)

print(Fore.LIGHTBLACK_EX + "\n[link terminated]" + Style.RESET_ALL)