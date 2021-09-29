import random
import subprocess
import os
import time
import sys
import json
import termcolor
#So you don't get a RecrsionError
sys.setrecursionlimit(10**6)#10 to the power of 6.
#^^^^^^^^^^^^^^^^^^^^^^^^^^^
from platform import system
def clear():
	if system() == 'Windows':
		cmd = 'cls'
	else:
		cmd = 'clear'
	subprocess.call(cmd, shell=True)
	return 0

global activities
if os.path.isdir('LanguageArts_DATA'):
	os.mkdir('LanguageArts_DATA')
def mainMenu():
	print('''
	Language Arts Programs,
	by Damien B.

	1 - Word Sorter
	2 - Letter Code Maker
	3 - Waterfall Maker

	\/ ENTER CHOICE \/
	''')
	a = int(input('> '))
	if a == 1:
		word = ''
		words = []
		clear()
		print('Word Sorter,')
		print('by Damien B.')
		print()
		print('(Enter your words and then input "exit" to exit.)\n\n')
		while True:
			word = input('Enter a word: ')
			if word != 'exit':
				words.append(word)
			else:
				break
		print('Sorting words...')
		words.sort()
		print('Words sorted.\n\nHere are your sorted words:')
		for word in words:
			print(word)
		print()
		print('Done.')
	elif a == 2:
		global letters
		letters = [
			'A',
			'B',
			'C',
			'D',
			'E',
			'F',
			'G',
			'H',
			'I',
			'J',
			'K',
			'L',
			'M',
			'N',
			'O',
			'P',
			'Q',
			'R',
			'S',
			'T',
			'U',
			'V',
			'W',
			'X',
			'Y',
			'Z'
		]
		global key
		key = {
			'A': None,
			'B': None,
			'C': None,
			'D': None,
			'E': None,
			'F': None,
			'G': None,
			'H': None,
			'I': None,
			'J': None,
			'K': None,
			'L': None,
			'M': None,
			'N': None,
			'O': None,
			'P': None,
			'Q': None,
			'R': None,
			'S': None,
			'T': None,
			'U': None,
			'V': None,
			'W': None,
			'X': None,
			'Y': None,
			'Z': None
		}
		def getRandomLetter(a: str):
			b = random.choice(letters)
			for c in key:
				if key[c] == b:
					print(termcolor.colored('Failure.  (Letter '+c+' for letter '+a+'.', 'red'))
					time.sleep(0.05)
					return getRandomLetter(a)
				else:
					print(termcolor.colored('Success.  (Letter '+c+' for letter '+a+'.', 'green'))
					time.sleep(0.05)
			return b
		

					
		for letter in letters:
			key[letter] = getRandomLetter(letter)
		print('Randomly generated key is:')
		for i in key:
			print(termcolor.colored(i, 'red')+':   '+termcolor.colored(key[i], 'green'))
		print('\n\n\n')
		words = []
		word = ''
		while True:
			word = input('Enter a word: ')
			if word != 'exit':
				words.append(word)
			else:
				break
		for a in words:
			b = words[a]
			b.upper()
			for c in range(len(b)):
				d =  b[c]
				b[c] = key[d]
				e = b[c]
				sys.stdout.write(e)
		print()
mainMenu()