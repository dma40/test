
import copy

class Sudoku:
    """A class meant to model a Sudoku board, 
    and which is capable of returning all solutions to a given board.
    """

    grid: list[list[int]]
    digits: list[int]

    def __init__(self, grid: list[list[int]], digits: list[int]) -> None:
        """
        Preconditions:

        - grid is a valid 9x9 Sudoku grid satisfying the rules of a valid Sudoku board
        (with empty spaces being denoted with 0)
        - digits contains the set of 9 digits (out of 0-9) that will be used to populate the Sudoku board.
        - The given grid is solvable (i.e. has at least one solution that satisfies Sudoku rules)
        """
        self.grid = grid
        self.digits = digits

    def __str__(self) -> str:
        return ("Grid: " + str(self.grid)
                + "\nDigits: " + str(self.digits))
    
    # Methods that check if a certain placement is viable
    # maybe also add a wrapper class Grid that has all of these methods in them

    def _has_digit(self, row: int, col: int) -> bool:
        """
        Returns if the given grid has a digit there.
        """
        return self.grid[row][col] != -1

    def _check_row_and_col(self, digit: int, row: int, col: int) -> bool:
        """
        This checks if the desired digit can be placed in the desired row and column.
        """
        
        for i in range(0, len(self.grid)):
            if self.grid[row][i] == digit and col != i:
                return False
            
        for j in range(0, len(self.grid)):
            if self.grid[j][col] == digit and row != j:
                return False
                
        return True
    
    def _check_square(self, digit: int, row: int, col: int) -> bool:
        """
        Determines whether the given digit can be placed in row row and 
        col col.
        """

        xpos = row // 3
        ypos = col // 3

        for i in range(3 * xpos, 3 * xpos + 3):
            for j in range(3 * ypos, 3 * ypos + 3):
                if self.grid[i][j] == digit:
                    return False
            
        return True
        
    def _can_place(self, digit: int, row: int, col: int) -> bool:
        return (self._check_square(digit, row, col) and 
                self._check_row_and_col(digit, row, col))
    
    # Helper methods for solving the sudoku

    def _is_contradiction(self, row: int, col: int) -> bool:
        """
        This determines if you have a empty square where nothing can be placed in a Sudoku grid
        (which is common when you have a unsolvable grid - you will reach situations
        where nothing can be placed)
        """
        if self._has_digit(row, col):
            for digit in self.digits:
                if self._can_place(digit, row, col):
                    return False
            return True
        return False
    
    def solved(self) -> bool:
        """
        Checks if the grid has been successfully solved.
        """
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] == -1:
                    return False
        return True
    
    def find_empty(self) -> tuple[int, int]:
        """
        Precondition: this grid has a empty square.
        """
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] == -1:
                    return (i, j)
        return (0, 0)
    
    # Method to find all possible solutions

    def solve(self) -> list[list[list[int]]]:
        """
        Return a list of all solved grids.
        """
        result = []
        
        if self.solved():
            g = copy.deepcopy(self.grid)
            return [g]
        else:
            x, y = self.find_empty()
            if self._is_contradiction(x, y):
                return []
            else:
                for number in self.digits:
                    if self._can_place(number, x, y):
                        self.grid[x][y] = number
                        result.extend(self.solve())
                        self.grid[x][y] = -1
        
        return result

# Test: NYT Medium Sudoku 

if __name__ == '__main__':
    sudoku = Sudoku([[-1, -1, -1, 8, -1, -1, -1, 6, -1],
                     [1, -1, 5, -1, -1, -1, -1, 9, -1],
                     [-1, 2, -1, 3, 4, -1, -1, -1, -1],
                     [-1, -1, -1, -1, -1, -1, -1, 1, -1],
                     [-1, -1, 3, -1, 2, -1, -1, 7, -1],
                     [-1, -1, -1, 1, -1, -1, 6, -1, 3],
                     [-1, -1, -1, -1, -1, 1, -1, -1, -1],
                     [-1, 5, -1, -1, -1, 8, -1, -1, 9],
                     [-1, 9, -1, -1, -1, 6, -1, 3, -1]], 
                    [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    s = sudoku.solve()
    print(len(s))
    print('\n')
    print("Solution\n")
    for i in range(0, len(s)):
        print(s[i])
        print('\n')
    
    
