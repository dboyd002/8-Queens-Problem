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

# Returns true if a move to a given index is within the bounds of the board
def is_valid_index(row, col):
    return 0 <= row < 8 and 0 <= col < 8

# Generates the set of neighbor states from a given state; all legal moves column-wise
def generate_neighbor_states(board_state):
    
    neighbor_states_set = []

    for col in range(8):
        
        for row in range(8):
            
            if board_state[row][col] == '1':
                
                for new_row in range(8):

                    if new_row != row and board_state[new_row][col] != '1':
                        
                        neighbor_board_state = copy.deepcopy(board_state)
                        neighbor_board_state[row][col] = '0'
                        neighbor_board_state[new_row][col] = '1'
                        neighbor_states_set.append(neighbor_board_state)

    return neighbor_states_set

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

# Returns whether a more fit state was found, which state was the most fit from an initial state and a set of neighbor states, and the fitness value of that state.
def find_most_fit_state(initial_state):
    
    most_fit_state = initial_state
    most_fit_state_value = evaluate_pairwise_fitness(initial_state)

    neighbor_states_set = generate_neighbor_states(initial_state)

    for neighbor_state in neighbor_states_set:
        
        fitness = evaluate_pairwise_fitness(neighbor_state)

        if fitness < most_fit_state_value:
            most_fit_state = neighbor_state
            most_fit_state_value = fitness

    # Check if the state changed
    state_changed = most_fit_state != initial_state

    return state_changed, most_fit_state, most_fit_state_value

def print_board_state(board_state):

    for row in board_state:
        print(' '.join(row))

    print("---------------")

# Returns True if a solution was found
def hill_climbing_search(num_queens, do_print):

    # Generate starting state
     state_to_check = generate_random_state(num_queens)

     # Generate the set of neighbors to the initial state
     neighbor_state_set = generate_neighbor_states(state_to_check)

     # State was changed from null to starting state
     state_changed = True

     # Continue generating neighbors and checking fitness each time a more fit neighbor is found
     while state_changed:
          
          state_changed, state_to_check, state_to_check_fitness_value = find_most_fit_state(state_to_check)

     if do_print:

          # Print the intitial state
          print_board_state(state_to_check)
          print("Fitness: " + str(evaluate_pairwise_fitness(state_to_check)) + '\n')
          print("^^INITIAL STATE^^\n")

          # Print the final state
          print_board_state(state_to_check)
          print("Fitness: " + str(state_to_check_fitness_value))
          print("\n^^FINAL STATE^^\n")

     solution_found = False

     # If the fitness of the final state is 0, return that a solution was found
     if state_to_check_fitness_value == 0:
         solution_found = True

     return solution_found

num_solutions_found = 0

# Run the search 100 times
for i in range(100):
    
    # Print the initial and final states of the first 10 times
    if i < 10:
        #PARAMS: number of queens, print bool
        solution_found = hill_climbing_search(32, True)
    elif i >= 10:
        #PARAMS: number of queens, print bool
        solution_found = hill_climbing_search(32, False)

    if solution_found:
        num_solutions_found += 1

print("Solutions Found: " + str(num_solutions_found))
    