from sudoku import Sudoku
from gcd import gcd_of_list, gcd

import copy

if __name__ == "__main__":

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exclusions = [1, 3, 4, 6, 7, 8, 9]

    for digit in exclusions:
        
        DIGITS = copy.deepcopy(digits)
        DIGITS.remove(digit)
        sudoku = Sudoku([[-1, -1, -1, -1, -1, -1, -1, 2, -1],
                         [-1, -1, -1, -1, 2, -1, -1, -1, 5],
                         [-1, 2, -1, -1, -1, -1, -1, -1, -1]
                         [-1, -1, 0, -1, -1, -1, -1, -1, -1]
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1]
                         [-1, -1, -1, 2, -1, -1, -1, -1, -1]
                         [-1, -1, -1, -1, 0, -1, -1, -1, -1]
                         [-1, -1, -1, -1, -1, 2, -1, -1, -1]
                         [-1, -1, -1, -1, -1, -1, -5, -1, -1]], 
                        DIGITS)
        
        solutions = sudoku.solve()