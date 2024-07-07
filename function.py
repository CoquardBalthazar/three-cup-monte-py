from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    #placeholder of the user guess :
    guess=' '
    
    #using while loop in order to repeat the question until the guess is valid. Using not in + list to get/ not different of
    while guess not in ['0','1','2']:
        guess = input("Pick a number between 0, 1 and 2 :  ")
        
    #return the guess of the player and save it as an integer 
    return int(guess)


def checking_guess(mylist, guess):
    if mylist[guess] == '0':
        print('Correct!')
    else:
        print('Wrong guess try again!')
        print(mylist)
