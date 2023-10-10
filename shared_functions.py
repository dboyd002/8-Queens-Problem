import random
import copy

def print_board_state(board_state):

    for row in board_state:
        print(' '.join(row))

    print("---------------")

# Generate a random board state representing num_queens queens with '1' and empty spaces with '0'
def generate_random_state(num_queens):

    if num_queens > 64:
            raise ValueError("Number of queens cannot exceed 64.")

    # Initialize an empty 8x8 grid
    random_state = [['0' for _ in range(8)] for _ in range(8)]

    col_counter = 0
    queens_placed = 0

    while queens_placed < num_queens:
         
         col = col_counter
         row = random.randint(0, 7)

         # Keep generating until the chosen space is not already occupied
         if random_state[row][col] == '0':
            random_state[row][col] = '1'
            queens_placed += 1
            col_counter += 1

            if col_counter > 7:
                 col_counter = 0

    return random_state

# Returns true if a move to a given index is within the bounds of the board
def is_valid_index(row, col):
    return 0 <= row < 8 and 0 <= col < 8

# Evaluates the fitness of a board state. Returns fitness == the number of pairwise attacks available on the board.
# Check all legal moves for each queen
def evaluate_pairwise_fitness(board_state):

     # Copy board state so that queens can be removed after finding an attack to achieve pairwise attacks
     copy_board_state = copy.deepcopy(board_state)
     
     fitness_value = 0
     
     for col in range(8):
          
          for row in range(8):
               
               if copy_board_state[row][col] == '1':
                    
                    # Check horizontal moves to the left of the queen
                    left_moves_counter = 1
                    while is_valid_index(row, col - left_moves_counter):

                        if copy_board_state[row][col - left_moves_counter] == '1':
                             fitness_value += 1
                             copy_board_state[row][col] = '0'
                             break
                        
                        left_moves_counter += 1

                    # Check horizontal moves to the right of the queen
                    right_moves_counter = 1
                    while is_valid_index(row, col + right_moves_counter):

                        if copy_board_state[row][col + right_moves_counter] == '1':
                             fitness_value += 1
                             copy_board_state[row][col] = '0'
                             break
                        
                        right_moves_counter += 1

                    # Check vertical moves below the queen
                    down_moves_counter = 1
                    while is_valid_index(row + down_moves_counter, col):

                        if copy_board_state[row + down_moves_counter][col] == '1':
                             fitness_value += 1
                             copy_board_state[row][col] = '0'
                             break
                        
                        down_moves_counter += 1

                    # Check vertical moves above the queen
                    up_moves_counter = 1
                    while is_valid_index(row - up_moves_counter, col):

                        if copy_board_state[row - up_moves_counter][col] == '1':
                             fitness_value += 1
                             copy_board_state[row][col] = '0'
                             break
                        
                        up_moves_counter += 1

                    # Check down-left diagonal moves from the queen
                    down_left_moves_counter = 1
                    while is_valid_index(row + down_left_moves_counter, col - down_left_moves_counter):

                        if copy_board_state[row + down_left_moves_counter][col - down_left_moves_counter] == '1':
                             fitness_value += 1
                             copy_board_state[row][col] = '0'
                             break
                        
                        down_left_moves_counter += 1

                    # Check down-right diagonal moves from the queen
                    down_right_moves_counter = 1
                    while is_valid_index(row + down_right_moves_counter, col + down_right_moves_counter):

                        if copy_board_state[row + down_right_moves_counter][col + down_right_moves_counter] == '1':
                             fitness_value += 1
                             copy_board_state[row][col] = '0'
                             break
                        
                        down_right_moves_counter += 1

                    # Check up-left diagonal moves from the queen
                    up_left_moves_counter = 1
                    while is_valid_index(row - up_left_moves_counter, col - up_left_moves_counter):

                        if copy_board_state[row - up_left_moves_counter][col - up_left_moves_counter] == '1':
                             fitness_value += 1
                             copy_board_state[row][col] = '0'
                             break
                        
                        up_left_moves_counter += 1

                    # Check up-right diagonal moves from the queen
                    up_right_moves_counter = 1
                    while is_valid_index(row - up_right_moves_counter, col + up_right_moves_counter):

                        if copy_board_state[row - up_right_moves_counter][col + up_right_moves_counter] == '1':
                             fitness_value += 1
                             copy_board_state[row][col] = '0'
                             break
                        
                        up_right_moves_counter += 1

     return fitness_value