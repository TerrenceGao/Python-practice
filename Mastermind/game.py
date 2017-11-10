from mastermind import *

if __name__ == '__main__':
    # the number of pegs in the answer
    SIZE = 4
    # the number of guesses the user gets
    TRIES = 10
    # the letters allowed representing the colours
    # green, red, blue, yellow, orange, purple
    VALID_CHARS = 'GRBYOP'

    # fill in the rest...
    #Create the secret colour code.
    answer=create_code(VALID_CHARS, SIZE)
    print(answer)
    guesslist = []
    cluelist = []
    count=0
    #Get the user's first guess
    for n in range(TRIES):
        count = count + 1
        guesslist.append(list(input("Please enter your guess of length 4 using the letters GRBYOP:")))
    #Check that the guess is valid
        if(valid(guesslist[n], VALID_CHARS, SIZE)==False):
            guesslist[n]=input("Please enter your guess again of length 4 using the letters GRBYOP:")
            guesslist[n]=list(guesslist[n])
    #Determine the appropriate clue for the guess
        bClues=find_fully_correct(answer, guesslist[n])
        wClues=find_colour_correct(answer, guesslist[n])
        cluelist.append(bClues+wClues)
    #Display the current state of the game including all guesses and clues.
        display_game(guesslist, cluelist)
        if(cluelist[n]==['b','b','b','b']):
            print("Congratulations! It took you",count,"guesses to find the code.")
            break
        elif(n==TRIES-1):
            print("I'm sorry you lose. The correct code was ",answer,'.')