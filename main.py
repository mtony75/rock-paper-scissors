# Program Rock-Paper-Scissors
# Accept a selection of rock, paper, scissors
# from a user then randomly select the same 
# choices and choose who wins.
#import random library
import random

def validChoice(choice):
	if (int(choice) < 1) | (int(choice) > 3):
		return False
	else:
		return True

def playAgain(game):
	if (int(game) == 1):
		return True
	else:
		return False

def getChoice():
	randomChoice=random.choice(['rock', 'paper', 'scisors'])
	return randomChoice
	
def rockVs(choice):
	if (choice == 'rock'):
		return 'tie'
	elif (choice =='paper'):
		return 'loose'
	else:
		return 'win'
	
def paperVs(choice):
	if (choice == 'rock'):
		return 'win'
	elif (choice == 'paper'):
		return 'tie'
	else:
		return 'loose'
	
def scissorsVs(choice):
	if (choice == 'rock'):
		return 'loose'
	elif (choice == 'paper'):
		return 'win'
	else:
		return 'tie'

def convertChoice(choice):
	if (int(choice) == 1):
		return 'rock'
	elif (int(choice) == 2):
		return 'paper'
	else:
		return 'scissors'
		
print('Lets Play \'Rock\' \'Paper\' \'Scissors\'')

# run controls the loop for game play. 1= go 0 = stop
run = 1
x = 5
while (run != 0):
	print('Your selections')
	print('1. Rock')
	print('2. Paper')
	print('3. Scissors')
	inputChoice = input('Enter your choice: ')
	if validChoice(inputChoice):
		usrChoice = convertChoice(inputChoice)
		print('Choice is valid')
		cpuChoice = getChoice()
		if (usrChoice == 'rock'):
			gameOutcome = rockVs(cpuChoice)
		elif (usrChoice == 'paper'):
			gameOutcome = paperVs(cpuChoice)
		else:
			gameOutcome = scissorsVs(cpuChoice)
		print('Player choose {}, the computer choose {}, so the player {}'.format(usrChoice,cpuChoice,gameOutcome))
	else:
		print('Choice not valid')
	print('Play another game?')
	print('1. Yes')
	print('2. No')
	nextGame = input('Choice: ')
	if playAgain(nextGame):
		run = 1
	else:
		run = 0
		
		

