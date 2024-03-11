#file : CS_A1_T2_3_20230527.PY
#Purpose : subtract a square game
# Author : Mawada Emad
# ID : 20230527





# get number of coins in the pile from the user
coins = int(input('Enter Number of coins in the pile: '))

player = 1  # player 1 starts the game
index = 1
# game loop
while coins > 0:

    print('Coins in the pile:', coins)         #display number of coins in the pile

    valid_moves = [i * i for i in range(1, coins + 1) if (i * i) <= coins]    #setting the valid moves
    
    print('Choose one of these moves:', valid_moves)             # display the available moves for the player to choose from
    
    move = int(input('Player ' + str(player) + '\'s move: '))            #get the player's move

    if index == 1  and  valid_moves[-1] == move :
        print(" you cannot take all the coins in one move")
        continue 
    # making sure the player chose the right move
    while move not in valid_moves or move > coins:                    
        if move not in valid_moves:
            print('Rejected, please select a valid move.')
    
        else:
            print('Rejected, you cannot take all the coins in one move.')
        move = int(input('Player ' + str(player) + '\'s move: '))            
    
    # updating number of coins in the pile after each move
    coins = coins - move

    player = 3 - player  # Switching players 
    index += 1

print('Player ' + str(3 - player) + ' wins')      # display the winner
