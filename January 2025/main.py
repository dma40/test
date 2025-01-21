from sudoku import Sudoku
from gcd import gcd_of_list, sudoku_grid_to_list

import copy

if __name__ == "__main__":

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exclusions = [1, 3, 4, 6, 7, 8, 9]

    GLOBAL_MAX_GCD = -1
    GLOBAL_MAX_GRID = []

    for digit in exclusions:
        
        max = -1
        localmax, local_max_grid = -1, []
        DIGITS = copy.deepcopy(digits)
        DIGITS.remove(digit)
        sudoku = Sudoku([[-1, -1, -1, -1, -1, -1, -1, 2, -1],
                         [-1, -1, -1, -1, 2, -1, -1, -1, 5],
                         [-1, 2, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, 0, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, 2, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, 0, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, 2, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, 5, -1, -1]], 
                        DIGITS)
        
        solutions = sudoku.solve()
        for solution in solutions:
            numbers = sudoku_grid_to_list(solution)
            localmax = gcd_of_list(numbers)
            if localmax > max:
                max, local_max_grid = localmax, solution

        if max > GLOBAL_MAX_GCD:
            GLOBAL_MAX_GCD, GLOBAL_MAX_GRID = max, local_max_grid
        
        print('\n')
        print(GLOBAL_MAX_GCD)

    print(GLOBAL_MAX_GRID)
    print('\n')
    for i in range(0, len(GLOBAL_MAX_GRID)):
        print(GLOBAL_MAX_GRID[4][i])

