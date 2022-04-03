from components.quizQuestions import questions
from components import gamevars, quizTally
from emoji import emojize

def rungame():

	answer1 = questions["q1"][input(questions["q1"]["question"])]
	print(answer1)

	gamevars.quizTotal += answer1
	print(emojize(":star:*－:+:－:+:－:+:－:+:－:+:－:+:－ :star: *－:+:－:+:－:+:－:+:－:+:－:+:－:star: \n"))

	answer2 = questions["q2"][input(questions["q2"]["question"])]
	print(answer2)

	gamevars.quizTotal += answer2
	print(emojize(":star:*－:+:－:+:－:+:－:+:－:+:－:+:－ :star: *－:+:－:+:－:+:－:+:－:+:－:+:－:star: \n"))

	answer3 = questions["q3"][input(questions["q3"]["question"])]
	print(answer3)

	gamevars.quizTotal += answer3
	print(emojize(":star:*－:+:－:+:－:+:－:+:－:+:－:+:－ :star: *－:+:－:+:－:+:－:+:－:+:－:+:－:star: \n"))

	answer4 = questions["q4"][input(questions["q4"]["question"])]
	print(answer4)

	gamevars.quizTotal += answer4
	print(emojize(":star:*－:+:－:+:－:+:－:+:－:+:－:+:－ :star: *－:+:－:+:－:+:－:+:－:+:－:+:－:star: \n"))
	
