import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    infile = open(WORDLIST_FILENAME, 'r')
    line = infile.readline()
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list


def choose_word(word_list):
    return random.choice(word_list)


def is_word_guessed(secretword, letters_guessed):
    word = ''
    for c in secretword:
        if c in letters_guessed:
            word += c
    if word == secretword:
        return True
    else:
        return False


def get_guessed_word(secretword, letters_guessed):
    result = ' '
    found = False
    for c in secretword:
        for j in letters_guessed:
            if c == j:
                result += c
                found = True
        if not found:
            result += '_ '
        found = False
    return result


def get_available_letters(letters_guessed):
    store = ''
    for l in string.ascii_lowercase:
        if l not in letters_guessed:
            store += l
    return store
    

def hangman(secretword):
    line = "-------------"
    letters_guessed = []
    guesses = 6
    word_guessed = False

    print("Welcome to Hangman!")
    print("I am thinking of a word that is " + str(len(secretword)) + " letters long.")
    print(line)

    while guesses > 0:
        if is_word_guessed(secretword, letters_guessed) == True:
            print('Congratulations, you won!')
            break
        else:
            print("You have " + str(guesses) + " guesses remaining.")
            print("Available letters: " + get_available_letters(letters_guessed))
            guess = input("Please guess a letter: ").lower()
            if guess in secretword:
                if guess in letters_guessed:
                    print("Oops! You've already guessed that letter: " + str(get_guessed_word(secretword, letters_guessed)))
                    print(line)
                else:
                    letters_guessed.append(guess)
                    print('Good guess: ' + str(get_guessed_word(secretword, letters_guessed)))
                    print(line)
            else:
                if guess in letters_guessed:
                    print("Oops! You've already guessed that letter: " + str(get_guessed_word(secretword, letters_guessed)))
                    print(line)
                else:
                    letters_guessed.append(guess)
                    guesses -= 1
                    print('Oh no! That letter is not in my word :( ' + str(get_guessed_word(secretword, letters_guessed)))
                    print(line)
    if guesses == 0:
        print('Sorry, you ran out of guesses. The word was \"' + secretword + '\"')

wordlist = load_words()
secretword = choose_word(wordlist).lower()
hangman(secretword)