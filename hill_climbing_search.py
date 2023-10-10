import random
import copy
import argparse

import shared_functions

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

# Returns whether a more fit state was found, which state was the most fit from an initial state and a set of neighbor states, and the fitness value of that state.
def find_most_fit_state(initial_state):
    
    most_fit_state = initial_state
    most_fit_state_value = shared_functions.evaluate_pairwise_fitness(initial_state)

    neighbor_states_set = generate_neighbor_states(initial_state)

    for neighbor_state in neighbor_states_set:
        
        fitness = shared_functions.evaluate_pairwise_fitness(neighbor_state)

        if fitness < most_fit_state_value:
            most_fit_state = neighbor_state
            most_fit_state_value = fitness

    # Check if the state changed
    state_changed = most_fit_state != initial_state

    return state_changed, most_fit_state, most_fit_state_value

# Returns True if a solution was found
def hill_climbing_search(num_queens, do_print):

    # Generate starting state
     state_to_check = shared_functions.generate_random_state(num_queens)

     # Generate the set of neighbors to the initial state
     neighbor_state_set = generate_neighbor_states(state_to_check)

     # State was changed from null to starting state
     state_changed = True

     # Continue generating neighbors and checking fitness each time a more fit neighbor is found
     while state_changed:
          
          state_changed, state_to_check, state_to_check_fitness_value = find_most_fit_state(state_to_check)

     if do_print:

          # Print the intitial state
          shared_functions.print_board_state(state_to_check)
          print("Fitness: " + str(shared_functions.evaluate_pairwise_fitness(state_to_check)) + '\n')
          print("^^INITIAL STATE^^\n")

          # Print the final state
          shared_functions.print_board_state(state_to_check)
          print("Fitness: " + str(state_to_check_fitness_value))
          print("\n^^FINAL STATE^^\n")

     solution_found = False

     # If the fitness of the final state is 0, return that a solution was found
     if state_to_check_fitness_value == 0:
         solution_found = True

     return solution_found

num_solutions_found = 0

def main():

    parser = argparse.ArgumentParser(description='Hill Climbing Search for the N-Queens Problem')
    parser.add_argument('num_queens', type=int, help='Number of queens on the board')
    parser.add_argument('num_runs', type=int, help='Number of times to run the search')

    args = parser.parse_args()

    num_solutions_found = 0

    for i in range(args.num_runs):
        
        # Call your hill_climbing_search function with the provided arguments
        solution_found = hill_climbing_search(args.num_queens, i < 10)
        
        if solution_found:
            num_solutions_found += 1

    print("Solutions Found: " + str(num_solutions_found))

if __name__ == '__main__':
    main()