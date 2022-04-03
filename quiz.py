from components.quizQuestions import questions
from components import gamevars, rungame, quizTally, gameend
from PIL import Image
from emoji import emojize 
from colorama import init, Fore, Back, Style

while gamevars.character is False:

	init(autoreset=True)
	print(emojize(":sparkles:====================:star::star::star: Welcome to the World of Marvel :star::star::star:====================:sparkles:"))
	print(Back.MAGENTA + "											")
	print(Back.MAGENTA + "											")
	print(emojize(Back.MAGENTA + "  :full_moon::full_moon::full_moon: Do you want to play the quiz of Marvel? type Y to play Or quit to exit :full_moon::full_moon::full_moon:  "))
	print(Back.MAGENTA + "											")
	print(Back.MAGENTA + "											")
	print("========================================================================================")

	gamevars.character = input(emojize("Please let me know your choice :eyes: : \n"))

	if gamevars.character == "quit":
		print(emojize(":neutral_face: You chose to quit :neutral_face:"))
		exit()

	elif gamevars.character == "Y":

		rungame.rungame()

		print(emojize(":sparkles::sparkles::sparkles:Hey~you got: " + str(gamevars.quizTotal) + ":sparkles::sparkles::sparkles:\n"))

		quizTally.total(gamevars.quizTotal)

		gamevars.quizTotal=0

		gameend.gameend()

		gamevars.character = False

	else:
		print("Please choose - Y or quit?")
		gamevars.character = input("Y / quit? ")
		gamevars.character = False



			
		
