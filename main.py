import random
import copy

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

def is_valid_index(row, col):
    return 0 <= row < 8 and 0 <= col < 8

# Generates the set of neighbor states from a given state
def generate_neighbor_states(board_state):
     
     neighbor_states_set = []
     
     for col in range(8):
          
          for row in range(8):
               
               if board_state[row][col] == '1':
                    
                    neighbor_board_state = copy.deepcopy(board_state)

                    up_counter = 0
                    while is_valid_index(row - up_counter - 1, col):
                         
                         if neighbor_board_state[row - up_counter - 1][col] == '0':

                            neighbor_board_state[row - up_counter][col] = '0'
                            neighbor_board_state[row - up_counter - 1][col] = '1'
                            neighbor_states_set.append(neighbor_board_state)

                         up_counter += 1

                    down_counter = 0
                    while is_valid_index(row + down_counter + 1, col):
                         
                         if neighbor_board_state[row + down_counter + 1][col] == '0':

                            neighbor_board_state[row + down_counter][col] = '0'
                            neighbor_board_state[row + down_counter + 1][col] = '1'
                            neighbor_states_set.append(neighbor_board_state)

                         down_counter += 1

     return neighbor_states_set


# Evaluates the fitness of a board state. Fitness == the number of pairwise attacks available on the board.
def evaluate_pairwise_fitness(board_state):
     
     fitness_value = 0
     
     for col in range(8):
          
          for row in range(8):
               
               if board_state[row][col] == '1':
                    
                    # Check horizontal moves to the left of the queen
                    left_moves_counter = 1
                    while is_valid_index(row, col - left_moves_counter):

                        if board_state[row][col - left_moves_counter] == '1':
                             fitness_value += 1
                             break
                        
                        left_moves_counter += 1

                    # Check horizontal moves to the right of the queen
                    right_moves_counter = 1
                    while is_valid_index(row, col + right_moves_counter):

                        if board_state[row][col + right_moves_counter] == '1':
                             fitness_value += 1
                             break
                        
                        right_moves_counter += 1

                    # Check vertical moves below the queen
                    down_moves_counter = 1
                    while is_valid_index(row + down_moves_counter, col):

                        if board_state[row + down_moves_counter][col] == '1':
                             fitness_value += 1
                             break
                        
                        down_moves_counter += 1

                    # Check vertical moves above the queen
                    up_moves_counter = 1
                    while is_valid_index(row - up_moves_counter, col):

                        if board_state[row - up_moves_counter][col] == '1':
                             fitness_value += 1
                             break
                        
                        up_moves_counter += 1

                    # Check down-left diagonal moves from the queen
                    down_left_moves_counter = 1
                    while is_valid_index(row + down_left_moves_counter, col - down_left_moves_counter):

                        if board_state[row + down_left_moves_counter][col - down_left_moves_counter] == '1':
                             fitness_value += 1
                             break
                        
                        down_left_moves_counter += 1

                    # Check down-right diagonal moves from the queen
                    down_right_moves_counter = 1
                    while is_valid_index(row + down_right_moves_counter, col + down_right_moves_counter):

                        if board_state[row + down_right_moves_counter][col + down_right_moves_counter] == '1':
                             fitness_value += 1
                             break
                        
                        down_right_moves_counter += 1

                    # Check up-left diagonal moves from the queen
                    up_left_moves_counter = 1
                    while is_valid_index(row - up_left_moves_counter, col - up_left_moves_counter):

                        if board_state[row - up_left_moves_counter][col - up_left_moves_counter] == '1':
                             fitness_value += 1
                             break
                        
                        up_left_moves_counter += 1

                    # Check up-right diagonal moves from the queen
                    up_right_moves_counter = 1
                    while is_valid_index(row - up_right_moves_counter, col + up_right_moves_counter):

                        if board_state[row - up_right_moves_counter][col + up_right_moves_counter] == '1':
                             fitness_value += 1
                             break
                        
                        up_right_moves_counter += 1

     return fitness_value

# Determines the most fit state from an initial state and its set of neighbor states
# def find_most_fit_state(initial_state):
       
#        # Flag to determine if a new most fit state was found
#        state_changed = False

#        # Initial state starts as the most fit state
#        most_fit_state = initial_state
#        most_fit_state_value = evaluate_pairwise_fitness(initial_state)

#        neighbor_states_set = generate_neighbor_states(initial_state)

#        for i in range(0, len(neighbor_states_set)):
            
#             fitness = evaluate_pairwise_fitness(neighbor_states_set[i])

#             if fitness < most_fit_state_value:
#                  most_fit_state = neighbor_states_set[i]
#                  most_fit_state_value = fitness
#                  state_changed = True

#        return state_changed, most_fit_state, most_fit_state_value

def find_most_fit_state(initial_state):
    
    most_fit_state = initial_state
    most_fit_state_value = evaluate_pairwise_fitness(initial_state)

    neighbor_states_set = generate_neighbor_states(initial_state)

    for neighbor_state in neighbor_states_set:
        fitness = evaluate_pairwise_fitness(neighbor_state)

        if fitness < most_fit_state_value:
            most_fit_state = neighbor_state
            most_fit_state_value = fitness

    state_changed = most_fit_state != initial_state  # Check if the state changed

    print(state_changed)

    return state_changed, most_fit_state, most_fit_state_value

def print_board_state(board_state):

    print("---------------\n")

    for row in board_state:
        print(' '.join(row))

# Starting state
state_to_check = generate_random_state(12)
neighbor_state_set = generate_neighbor_states(state_to_check)

state_changed = True

while state_changed:
     
    state_changed, state_to_check, state_to_check_fitness_value = find_most_fit_state(state_to_check)
    print_board_state(state_to_check)
    print(state_to_check_fitness_value)
