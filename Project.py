# Main Board 
def display(v):
    print("\n"*10)
    print(" "+v[7]+" | "+v[8]+" | "+v[9])
    print(" "+v[4]+" | "+v[5]+" | "+v[6])
    print(" "+v[1]+" | "+v[2]+" | "+v[3])
    print("\n")

# X or O selection   
def select_X_O():
    
    choice = ''
    
    while choice not in ['X','O']:
        choice = input("Player1 choose your option 'X' or 'O': ").upper()
        
        # Wrong input
        if choice not in ['X','O']:
            print("Ops! select 'X' or 'O'")
        
    if choice == 'X':
        return('X','O')
    else:
        return('O','X')


import random

# Random player selection
def ran_player():
    
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'
        
# Merge with board      
def fixing(board,position,element):
    board[position] = element
    
    return board

# Win condition checking
def win(board,ele):

    return ((board[1]==ele and board[2]==ele and board[3]==ele) or # bottom row
    (board[4]==ele and board[5]==ele and board[6]==ele) or         # middle row
    (board[7]==ele and board[8]==ele and board[9]==ele) or         # top row
    (board[1]==ele and board[4]==ele and board[7]==ele) or         # first col
    (board[2]==ele and board[5]==ele and board[8]==ele) or         # second col
    (board[3]==ele and board[6]==ele and board[9]==ele) or         # third col
    (board[1]==ele and board[5]==ele and board[9]==ele) or         # diagonal /
    (board[3]==ele and board[5]==ele and board[7]==ele))           # diagonal \

# Board Space is free or not
def space_check(board,position):
    return board[position] == ' '

# board is full or empty
def full_emp(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# Box position choice
def box_position(board):
    
    choice = ''
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        choice = input("Select your position from 1-9: ")
        
        # Data checking
        if choice.isdigit() == False:
            print("Ops! Select position from 1-9")
        
        # Range checking
        if choice.isdigit() == True:
            if int(choice) not in range(1,10):
                print("Out of range! from 1-9")
            else:
                # Space checking
                if space_check(board,int(choice)):
                    within_range = True
                else:
                    print("That position is already full!")
    return int(choice)
        
# Play again or not
def replay():
    
    return input("Do you want to play again? 'Y'es or 'N'o: ").upper().startswith('Y')
        

# Final GAME LOGIC
 
print("Welcome to TIC TAC TOE")
print("\n")

while True:
    
    # Create board
    board = [' '] * 10
    
    # X,O input
    Player1,Player2 = select_X_O()
    
    # Random player selection
    turn = ran_player()
    print(turn + " goes to play first :)")
    
    # Ready or not
    ready = input("Are you ready? 'Y'es or 'N'o: ").upper()
    
    if ready == 'Y' or ready.startswith('Y'):
        game_on = True
    else:
        game_on = False

    # Game start
    while game_on:
        
        if turn == 'Player1':
            
            # Display board 
            display(board)
            
            # Box position
            pos = box_position(board)
            
            # Fixing with box
            fixing(board,pos,Player1)
            
            # Win checking
            if win(board,Player1):
                display(board)
                print("Player1 won the Game!!")
                break
            else:
                # Full or empty
                if full_emp(board):
                    display(board)
                    print("Match Draw!!")
                    break
                else:
                    # Change player
                    turn = 'Player2'
        
        else:
            
            # Display board 
            display(board)
            
            # Box position
            pos = box_position(board)
            
            # Fixing with box
            fixing(board,pos,Player2)
            
            # Win checking
            if win(board,Player2):
                display(board)
                print("Player2 won the Game!!")
                break
            else:
                # Full or empty
                if full_emp(board):
                    display(board)
                    print("Match Draw!!")
                    break
                else:
                    # Change player
                    turn = 'Player1'
                    
    if not replay():
        break

