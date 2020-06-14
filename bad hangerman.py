import random

WORDS = ['hello', 'tanya', 'zhopa', 'suchka', 'shushary']
MISTAKES_ALLOWED = 6

def random_word():
    return random.choice(WORDS)

def user_input():
    letter_input = input('Type letter: ')
    return letter_input

def get_statuses(word):
	statuses = []
	for letter in word:
		statuses.append(False)
	return statuses



def game_over(statuses, mistakes_counter):



def GAME():
    mistakes_counter = 0
    word = random_word()
    statuses = get_statuses(word)
    while not game_over(statuses, mistakes_counter):
        typed_letter = user_input()
        print_word(word, statuses)
GAME()

