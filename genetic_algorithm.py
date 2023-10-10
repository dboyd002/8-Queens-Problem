import random
import copy

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

def genetic_algorithm():

    # Generate initial population (2 parents)
    parent_1 = shared_functions.generate_random_state()
    parent_2 = shared_functions.generate_random_state()

    # Perform initial crossover resulting in 2 children
    child_1, child_2 = crossover(parent_1, parent_2)

    # Evaluate the fitness of both parents and both children and remove the two lowest

