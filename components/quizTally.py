from components import gamevars
from PIL import Image
from emoji import emojize
from colorama import init, Fore, Back, Style

def total(value):

    if value == 30:
        gamevars.character = gamevars.characters[0]

        print(emojize(Fore.RED + "You are :alien:  " + gamevars.character))
        spider_man = Image.open("spider_man.png")
        spider_man.show()

    if value <= 20:
        gamevars.character = gamevars.characters[1]

        print(emojize(Fore.CYAN + "You are :cyclone:  " + gamevars.character))
        captain_america = Image.open("captain_america.png")
        captain_america.show()

    if value >= 50:
        gamevars.character = gamevars.characters[2]

        print(emojize(Fore.GREEN + "You are :man:  "+ gamevars.character))
        dr_strange = Image.open("doctor_strange.png")
        dr_strange.show()