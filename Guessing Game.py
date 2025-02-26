# import random module
import random

# generate a random number between 0 and 7
choice = random.randint(0, 7)

# create a dictionary of random clues
random_clues = {
    0: 'My passion in life',
    1: 'The best story book',
    2: 'The old continent',
    3: 'The destroyer of worlds',
    4: 'The most popular programming language',
    5: 'The strongest bite in the animal world',
    6: 'The continent with the most natural resources',
    7: 'The most important company in the world'
}

# select a random clue
clue = random_clues[choice]

# create a dictionary of secret words
secret_word = {
    'My passion in life': 'programming',
    'The best story book': "the devil's spell",
    'The old continent': 'europe',
    'The destroyer of worlds': 'oppenheimer',
    'The most popular programming language': 'javascript',
    'The strongest bite in the animal world': 'crocodile',
    'The continent with the most natural resources': 'africa',
    'The most important company in the world': 'asml'
}

# create a dictionary of fun facts
fun_facts = {
    'programming': 'The first computer program was written in 1943 by Alan Turing and his team.',
    "the devil's spell": 'Come on it really is!',
    'europe': 'the Bill and Melinda Gates Foundation published their annual letter that highlights the surprises they saw in 2018. Europe had a median age of 42, 7 years above the nearest continent, which was North America.',
    'oppenheimer': 'Oppenheimer is the man resposible for the atomic bomb, he quoted the Bhagavad Gita, "Now I am become Death, the destroyer of worlds."',
    'javascript': r'JavaScript is used by 62.3% of developers worldwide.',
    'crocodile': r'The crocodile has a bite force of over 16k Newtons, more than 9 times that of a lion.',
    'africa': 'French and British colonialism turned Africa, the continent, the richest in natural resources, into the poorest continent in the world today',
    'asml': 'Dutch ASML is the sole supplier of photolithography machines, which are used in the production of computer chips.'
}

# select the secret word
fact = secret_word[clue]

# initialize variables
no_of_guesses = 1
score = 4

# print welcome message
print('Welcome to the guessing game! You have 3 chances to guess the secret word. Good luck!')

# ask user if they want a clue
decision = input('Do you want a clue? (type y for clue or press any button to continue): ')

# check if user wants a clue
if decision.lower() == 'y':
    print(clue)
    score = 3
else:
    print('You have chosen not to receive a clue. Good luck!')

# ask user to guess the secret word
guess = input('Guess the secret word: ')

# check if the guess is correct
while guess.lower() != secret_word[clue]:
    no_of_guesses += 1
    if no_of_guesses <= 3:
        guess = input('Guess again: ')
    else:
        print("You have run out of guesses. \nGoodluck next time!")
        break
else:
    print('Congratulations! You guessed the secret word!')
    score = score - no_of_guesses
    print('Your score is: ' + str(score))
    print(fun_facts[fact])

input('Press any key to exit')