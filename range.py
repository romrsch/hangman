import random
HANGMAN_PICS = ['''
+----+
	|

	|

	|

	|
   ====''','''
+----+
	|

	|

	|

	|
   ====''','''
+----+
 0	|

 |	|

	|

	|
   ====''','''
+----+
 0	|

/|	|

	|

	|
   ====''','''

+----+
 0	|

/|\	|

	|

	|
 ====''','''
+----+
 0	|

/|\	|

/	|

	|
 ====''','''
+----+
 0	|

/|\	|

/ \	|

	|
 ====''']

 words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лягушка медведь моллюск моль мул муравей мышь норка носорог обязьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()

 def getRandomWord(wordList):
 	# Эта функция возвращает случайную строку из переданного списка.
 	wordIndex = random.randint(0, len(wordList) - 1)
 	return wordList[wordIndex]

 def displayBoard(missedLetters, correctLetters, secretWord):
 	print(HANGMAN_PICS[len(missedLetters)])
 	print()

 	print('Ошибочные буквы:', end='')
 	for letter in missedLetters:
 		print(letter, end='')
 	print()


 	blanks = '_' *len(secretWord)

 	for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
 		if secretWord[i] in correctLetters:
 			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

 	for letter in blanks: # Показывает секретное слово с пробелами между буквами
 		print(letter, end='')
 		print()

 def getGuess(alreadyGuessed):
 	# Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше.

 	while True:
 		print('Введите букву.')
 		guess = input()
 		gues = guess.lower()

 		if len(guess) !=1:
 			print('Пожалуйста, введите одну букву.')

 


