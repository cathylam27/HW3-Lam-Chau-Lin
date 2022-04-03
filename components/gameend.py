from components import gamevars
from emoji import emojize

def gameend():

	gamevars.character = input(emojize(":warning:  Do you want to play again? Y/quit  :warning: \n"))

	if 	gamevars.character == "Y":
		gamevars.character = False

	elif gamevars.character == "quit":
		print(emojize(":neutral_face: You chose to quit :neutral_face:"))
		exit()

	else: 
		print("Please choose - Y or quit?")