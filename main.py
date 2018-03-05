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
	pass
	
def paperVs(choice):
	pass
	
def scissorsVs(choice):
	pass
		
print('Lets Play \'Rock\' \'Paper\' \'Scissors\'')

# run controls the loop for game play. 1= go 0 = stop
run = 1
x = 5
while (run != 0):
	print('Your selections')
	print('1. Rock')
	print('2. Paper')
	print('3. Scissors')
	usrChoice = input('Enter your choice: ')
	if validChoice(usrChoice):
		print('Choice is valid')
		cpuChoice = getChoice()
		if (usrChoice == 'rock'):
			
		
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
		
		

