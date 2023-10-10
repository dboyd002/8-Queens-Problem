import random
import copy
import argparse

import shared_functions

population = []

# Selects a random point and swaps its value between two boards
def crossover(board_1, board_2):

    row = random.randint(0, 7)
    col = random.randint(0, 7)

    board_1_value = board_1[row][col]
    board_2_value = board_2[row][col]

    child_1 = copy.deepcopy(board_1)
    child_2 = copy.deepcopy(board_2)

    child_1[row][col] = board_2_value
    child_2[row][col] = board_1_value

    return child_1, child_2

# Applies a configurable chance of mutation (a random space on the board swaps values)
def roll_for_mutation(board, percentage_odds):

    if percentage_odds > 100 or percentage_odds < 0:
            raise ValueError("Odds must be between 0 and 100 (percentage)")
    
    rand_roll = random.randint(1, 100)

    # Chance hit, swap value of a random space
    if rand_roll < percentage_odds:
         
         row = random.randint(0, 7)
         col = random.randint(0, 7)

         if board[row][col] == '0':
              board[row][col] = '1'
         elif board[row][col] == '1':
              board[row][col] = '0'

# Generates two children from two parents and returns the fittest two boards from the four
def iterate_generation(parent_1, parent_2):
     
     # Perform initial crossover resulting in 2 children
    child_1, child_2 = crossover(parent_1, parent_2)

    # 10% chance to mutate for each child
    roll_for_mutation(child_1, 10)
    roll_for_mutation(child_2, 10)

    # Evaluate the fitness of both parents and both children and remove the two lowest
    p_1_fitness = shared_functions.evaluate_pairwise_fitness(parent_1)
    p_2_fitness = shared_functions.evaluate_pairwise_fitness(parent_1)
    c_1_fitness = shared_functions.evaluate_pairwise_fitness(child_1)
    c_2_fitness = shared_functions.evaluate_pairwise_fitness(child_2)

    # Create a list of tuples containing fitness values and board states
    fitness_boards = [
        (p_1_fitness, parent_1),
        (p_2_fitness, parent_2),
        (c_1_fitness, child_1),
        (c_2_fitness, child_2)
    ]

    # Sort the list by fitness values
    sorted_fitness_boards = sorted(fitness_boards, key=lambda x: x[0])

    # Extract the fittest two board states
    fittest_board_1 = sorted_fitness_boards[0][1]
    fittest_board_2 = sorted_fitness_boards[1][1]

    shared_functions.print_board_state(fittest_board_1)
    print("Fitness:", sorted_fitness_boards[0][0])
    shared_functions.print_board_state(fittest_board_2)
    print("Fitness:", sorted_fitness_boards[1][0])

    solutions_found = 0

    if sorted_fitness_boards[0][0] == 0:
         solutions_found += 1

    if sorted_fitness_boards[1][0] == 0:
         solutions_found += 1

    return fittest_board_1, fittest_board_2, solutions_found

def genetic_algorithm(num_queens, num_generations):

    run_solutions_found = 0

    # Generate initial population (2 parents)
    parent_1 = shared_functions.generate_random_state(num_queens)
    parent_2 = shared_functions.generate_random_state(num_queens)

    for i in range(num_generations):
         
         parent_1, parent_2, solutions_found = iterate_generation(parent_1, parent_2)

         run_solutions_found += solutions_found

    return run_solutions_found

def main():

    parser = argparse.ArgumentParser(description='Genetic Algorithm for the N-Queens Problem')
    parser.add_argument('num_queens', type=int, help='Number of queens on the board')
    parser.add_argument('num_generations', type=int, help='Number of times to run the search')

    args = parser.parse_args()
        
    # Call your hill_climbing_search function with the provided arguments
    solutions_found = genetic_algorithm(args.num_queens, args.num_generations)

    print("Solutions Found: " + str(solutions_found))

if __name__ == '__main__':
    main()