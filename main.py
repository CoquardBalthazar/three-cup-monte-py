from random import shuffle
from function import shuffle_list, player_guess, checking_guess 

# Name the initial list
mylist = [' ','0',' ']

# Shuffle list : get the results as a new variable to be able to call it after
mix_list = shuffle_list(mylist)

# Guess of the player
guess = player_guess()

# Check the result = call the function and create the interaction between them
checking_guess(mix_list,guess)