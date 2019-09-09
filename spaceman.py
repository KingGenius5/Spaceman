import random

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
            counter +=1
    if counter == len(secret_word):
        return True
    else:
        return False
    #pass

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
    guessed_word = [i if i in letters_guessed else '_' for i in secret_word]
    return "".join(guessed_word)
    #pass


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
    #pass

def checkletter():
    while True:
        guess = input('Please input a letter: ').lower()
        if guess.isalpha():
            if len(guess)>1:
                print('That does not work : '+ guess)
                continue
            else:
                return guess
                break
        else:
            print('That does not work : '+ guess)
            continue

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost

    wordGuessed = False
    guess = ""
    letters_guessed = []
    guesses_left = len(secret_word)

    while guesses_left > 0 and guesses_left <= len(secret_word) and wordGuessed is False:
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            wordGuessed = True
            break
        print("You only have " + str(guesses_left) + " guesses left.")

        guess = checkletter()

        if guess in secret_word:
            if guess in letters_guessed:
                print ("You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
                
            else:
                letters_guessed.append(guess)
                print ('Great guess: ' + get_guessed_word(secret_word, letters_guessed))

        else:
            if guess in letters_guessed:
                print ("You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
                
            else:
                letters_guessed.append(guess)
                guesses_left-= 1
                print ('That letter is not in the word: ' + get_guessed_word(secret_word, letters_guessed))
                
    #Will use this for replaying game
    if wordGuessed == True:
        return 'Great job, you won!'
        
    elif guesses_left== 0:
        print ('Too bad, you do not have any more guesses. The word was ' + secret_word)



#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())