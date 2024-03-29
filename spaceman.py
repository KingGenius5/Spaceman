import random
from termcolor import colored

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('/Users/mtifak/Desktop/dev/words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    counter = 0
    for i in secret_word:
        if i in letters_guessed:
            counter += 1
    if counter == len(secret_word):
        return True
    else:
        return False

#TEST
def test_is_word_guessed():
    assert is_word_guessed('flamboyant',['f','l','a','m','b','o','y','n','t']) == True
    assert is_word_guessed('flamboyant',['a','e','i','o','u','f','z']) == False

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    
    #Had this piece of code at first but rewrote after Jess's lesson about code readability being better for more efficent and higher quality programming
    #guessed_word = [i if i in letters_guessed else ' _ ' for i in secret_word]
    #return "".join(guessed_word)

    guessed_word = []
    #i loops through each letter in the secret_word and checks if it is in letters they already guessed, then appending that to guessed_word
    for i in secret_word:
        if i in letters_guessed:
            guessed_word.append(i)
        else:
            guessed_word.append(' _ ')
    #From python doc, this lets us display all the list items in guessed_word as a string
    return ''.join(guessed_word)

#TEST
def test_get_guessed_word():
    assert get_guessed_word("flamboyant",['a','o','t','f','z','h']) == "f _ a _ _ o _ a _ t"
    assert get_guessed_word("flamboyant",['f','l','m','n']) == "fl _ m _ _ _ _ n _"


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if secret_word.find(guess) > 0:
        return True
    else:
        return False

#TEST
def test_is_guess_in_word():
    assert is_guess_in_word("a", "flamboyant") == True
    assert is_guess_in_word("z", "flamboyant") == False

#TODO: Ask the player to guess one letter per round and check that it is only one letter
def check_double_entry():
    '''
    A function that checks to see if the user has guessed only an indivual letter at each time (per input)
    If they enter a number, symbol, or more than one letter, it will return as invalid input
    '''
    while True:
        guess = input("Please enter a letter you think is in the mystery word: ").lower()
        if guess.isalpha():#checks to see if only alphabetical values are inputted (no numbers or symbols)
            if len(guess)>1:
                print("You can only enter one letter at a time : " + guess)
                continue
            else:
                return guess
                break
        else:
            print("You can only enter one letter at a time : " + guess)
            continue

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    wordGuessed = False
    guess = ""
    letters_guessed = []
    guesses_left = len(secret_word)

    while guesses_left > 0 and guesses_left <= len(secret_word) and wordGuessed is False:
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            wordGuessed = True
            break
        print("You currently have " + str(guesses_left) + " guesses left.")

        guess = check_double_entry()

        #TODO: show the guessed word so far
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if guess in secret_word:
            if guess in letters_guessed:
                print ("You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
                print("\n"+40*"-"+"\n")
                
            else:
                letters_guessed.append(guess)
                print("Letters guessed: " + ', '.join(letters_guessed))
                print ('Awesome guess: ' + get_guessed_word(secret_word, letters_guessed))
                print("\n"+40*"-"+"\n")

        else:
            if guess in letters_guessed:
                print ("You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
                print("\n"+40*"-"+"\n")
                
            else:
                letters_guessed.append(guess)
                print("Letters guessed: " + ', '.join(letters_guessed))
                guesses_left -= 1
                print ('That letter is not in the word: ' + get_guessed_word(secret_word, letters_guessed))
                print("\n"+40*"-"+"\n")
                
    #TODO: check if the game has been won or lost
    if wordGuessed == True:
        print("Ay" + colored("Congratulations", 'cyan') + ", you WON!")
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == "y":
            secret_word = load_word()
            spaceman(load_word())
        elif play_again == "n":
            print("Good-bye.")
        else:
            print("Not a valid input.")
        
    elif guesses_left == 0:
        print (colored("YOU LOST.", 'red') + " Alexa, this is so sad. The word was " + secret_word)
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == "y":
            secret_word = load_word()
            spaceman(load_word())
        elif play_again == "n":
            print("Good-bye!")
        else:
            print("Not a valid input.")

#TODO: show the player information about the game according to the project spec
print("\n"+50*"~")
print(13*"*"+colored(" WELCOME TO SPACEMAN!!! ",'green')+13*"*")
print(50*"~")
print("Let's play a word guessing game so we can save the spaceman.\n")

#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
