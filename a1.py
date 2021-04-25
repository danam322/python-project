# Da seo Min  501022491
# Assignment 1

# This is a script of a very simple game, Hangman. There is an hidden word and the player has to guess what it is.
# The player can guess a letter and the program will tell them if the word contains that letter or not. Or, they can
# guess a word and the program will let them know if it's right or wrong. Using these hints, the player
# should find out what the word is within the given tries.


def start():   # this is a function to start the Hangman game
    player = input("Hello there, what's your name? ")   # this asks for the player's name
    print("Hello", player + '!')   # it welcomes the player by calling his/her name
    play = input("Do you want to play Hangman? (y/n) ").lower()   # used the .lower() so the program runs without
    # error even if the player enters a capital letter
    if play == 'y':
        game(any)    # if the player enters y(yes) it'll call the game function and start the game
    else:     # if the player enters anything else than y, it'll quit saying 'Goodbye!'
        print('Goodbye!')

def game(word_to_guess):  # this is a function to play the game
    word_to_guess = 'world'   # there's only one possible word to guess for this game, which is 'world'
    word_to_guess = list(word_to_guess)  # this turns the string into a list
    lst = []    # this is an empty list to put all the letters of the word_to_guess
    lst.extend(word_to_guess)   # now all the letters are put into the empty list
    guessed = False   # this will later help the program know when the player has guessed the word correctly
    tries_left = 7  # the player will only have 7 tries to guess the word
    print("You have", tries_left, "tries.")
    for i in range(len(lst)): # each letter of the word_to_guess(a list) will turn into an underscore with
        lst[i] = "_ "     # a space right after to prevent the underscores to look like they are attached to each others
    print(''.join(lst))  # this joins the list into a string and lets the player see how many letters there are to guess
    while tries_left > 0 and guessed == False: # this while loop will run as long as the player doesn't run out of tries
        # and hasn't guessed the word yet
        guess = input("Take a guess, it could be a letter or a word: ").lower()
        # the player can put a letter or a word as an guess/input and it will read them as lower case
        if guess == ''.join(word_to_guess):
            # using .join(), it turns the word_to_guess into a string since it was a list
            # this if statement is for when the guess/input is a word
            guessed = True  # if the player's word guess matches the word_to_guess, guessed will become True
            break  # this will jump out of the while loop then proceed to the next command
        for j in range(len(word_to_guess)): # this for loop sets the range to the number of letters in the word_to_guess
            # this for loop is for when the guess/input is a letter
            if word_to_guess[j] == guess:  # if the letter guess matches one of the letters of the word_to_guess,
                lst[j] = guess + ' '  # it'll change the underscore from the list into the letter the player has guessed
                new = ''.join(lst)   # using the .join(), it creates a new string
                print(new)    # this prints the new string to show the player where the correctly guessed letter's spot
                print("You guessed it right!", guess, "is in the word!")
                if '_ ' not in lst:   # this if statement is for when all the letters were guessed correctly
                    guessed = True    # guessed will change to True and it'll jump out of the while loop since it
                    # no longer satisfies the condition
        if len(guess) > 1:  # this if statement is for when the player did not guess the word right
            print(guess, 'is not the answer.')
        if len(guess) == 1 and guess not in word_to_guess:
            # this if statement is for when the player did not guess the letter right
            print(''.join(lst))  # this prints the latest process of the player
            print(guess, 'is not in the word.')
            # this let's the player know that his/her guess wasn't in the word_to_guess
        tries_left -= 1  # everytime the player guesses the word correctly or not, the number of tries reduces by one
        # and whenever the number of tries turns to 0, it'll jump out of this while loop because it'll no longer
        # satisfy the condition
    if guessed == True:  # this if statement is for when guessed is True, in other words the player has guessed
        # the word correctly within the given tries
        print('You guessed the word, great job!')
    if tries_left == 0 and guessed == False:  # this if statement is for when the player has ran out of tries
        # and still wasn't able to guess the word
        print('Sorry, you ran out of tries. Try again next time :)')
        # it'll print that the player has lost and end the game
    return word_to_guess

if __name__ == "__main__":  # this tells the program that this is the main part of the whole script
    start()  # calling the start() function to let it start the Hangman game