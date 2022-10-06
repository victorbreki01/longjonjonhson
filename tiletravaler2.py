"""
1. Describe the general outline of how you're going to develop this program, and commit it.

2. Then gradually break it down into more detailed steps (committing after each comprehensive step),
until you start to see a way to convert this description into code.
"""

# 3. Then start writing the code
# direction options called while playing game.
N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'

# definers for tiles, directions and while loop
column, row = 1 , 1
direction_option = ('')
direction = ''
victory = False
baddirect = 0

def in_case(baddirect):
    if baddirect == 1:
        return print(f"You can travel: {N}.")
    elif baddirect == 2:
        return print(f"You can travel: {N} or {E} or {S}.")
    elif baddirect == 3:
         return print(f"You can travel: {E} or {S}.")
    elif baddirect == 4:
        return print(f"You can travel: {N}.")
    elif baddirect == 5:
        return print(f"You can travel: {S} or {W}.")
    elif baddirect == 6:
        return print(f"You can travel: {E} or {W}.")
    elif baddirect == 8:
        return print(f"You can travel: {N} or {S}.")
    elif baddirect == 9:
        return print(f"You can travel: {S} or {W}.")

def move(column, row, direction):
    ''' moving player through tiles based on input'''
    
    if direction == 'n':
        row += 1
    elif direction == 's':
        row -= 1
    elif direction == 'e':
        column += 1
    elif direction == 'w':
        column -= 1
    return column, row


def game(column, row, direction, direction_option, victory, baddirect):
    ''' while loop for player moving through the tiles'''
    counter = 0
    while not victory:
        if direction in direction_option:
		
            if ((column == 1) and (row == 1)): 
                print(f"You can travel: {N}.")
                direction_option = ('n')
                baddirect = 1

            elif (column == 1) and (row == 2):
                coin = coin_counter()
                if coin == True:
                    counter += 1
                    print(f"You received 1 coin, your total is now {counter}.")
                print(f"You can travel: {N} or {E} or {S}.")
                direction_option = ('n', 'e', 's')
                baddirect = 2
				
            elif (column == 1) and (row == 3):  
                print(f"You can travel: {E} or {S}.")
                direction_option = ('e', 's')
                baddirect = 3

            elif ((column == 2) and (row == 1)): 
                print(f"You can travel: {N}.")
                direction_option = ('n')
                baddirect = 4
				
            elif (column == 2) and (row == 2):
                coin = coin_counter()
                if coin == True:
                    counter += 1
                    print(f"You received 1 coin, your total is now {counter}.")
                print(f"You can travel: {S} or {W}.")
                direction_option = ('s', 'w')
                baddirect = 5
				
            elif (column == 2) and (row == 3):
                coin = coin_counter()
                if coin == True:
                    counter += 1
                    print(f"You received 1 coin, your total is now {counter}.")
                print(f"You can travel: {E} or {W}.")
                direction_option = ('e', 'w')
                baddirect = 6
			
            elif column == 3 and row == 1:  
                print(f'Victory! Total coins {counter}.')
                victory = True				

            elif (column == 3) and (row == 2):
                coin = coin_counter()
                if coin == True:
                    counter += 1
                    print(f"You received 1 coin, your total is now {counter}.")
                print(f"You can travel: {N} or {S}.")
                direction_option = ('n', 's')
                baddirect = 8

            elif (column == 3) and (row == 3):
                print(f"You can travel: {S} or {W}.")
                direction_option = ('s', 'w')
                baddirect = 9

        if victory != True:
            direction = str(input("Direction: "))
            direction = direction.lower()
            if direction in direction_option:
                column, row = move(column, row, direction)
            else:
                print('Not a valid direction!')
                in_case(baddirect)

def coin_counter():
    choice = input("Pull a lever (y/n): ")
    choice = choice.lower()
    if choice == "y":
        return True
    else:
        return False
# OK let's play
game(column, row, direction, direction_option, victory, baddirect) 