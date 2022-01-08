# Created by : Orel Rahum
from Live import *
import colorama
from colorama import Fore, init

##################################################################################################
# Console colors
W = '\033[0m'  # white
G = '\033[32m'  # green
##################################################################################################

init()
print(welcome(f"{G}Doron Nuni{W}"))
load_game()
