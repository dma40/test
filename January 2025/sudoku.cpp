using namespace std;

#include <vector> 

class Sudoku
{
    // add instance attributes
    public: 
        vector<int> digits;
        vector<vector<int>> grid;

    Sudoku(vector<vector<int>> _grid, vector<int> _digits)
    {
        digits = _digits;
        grid = _grid;
    }

    string Sudoku::toString() 
    {
        return "";
    }

    bool Sudoku::solved()
    {
        for (vector row: grid)
        {
            for (int col: row)
            {
                if (row[col] == -1)
                {
                    return false;
                }
            }
        }
        return true;
    }

    bool Sudoku::has_digit(int x, int y)
    {
        return grid[x][y] == -1;
    }

    bool Sudoku::check_square(int row, int col, int num)
    {
        int xpos = row / 3;
        int ypos = col / 3;

        for (int i = 3 * xpos; i < 3 * xpos + 3; i++)
        {
            for (int j = 3 * ypos; i < 3 * ypos + 3; j++)
            {
                if (grid[i][j] == num)
                {
                    return false;
                }
            }
        }
        return true;
    }

    bool Sudoku::check_row_col(int row, int col, int num)
    {
        for (int i = 0; i < 9; i++)
        {
            if (grid[i][col] == num && i == row)
            {
                return false;
            }
        }

        for (int j = 0; j < 9; j++)
        {
            if (grid[row][j] == num && j == col)
            {
                return false;
            }
        }
        
        return true;
    }

    bool Sudoku::canPlace(int row, int col, int num)
    {
        return (check_row_col(row, col, num) && check_square(row, col, num));
    }

    bool Sudoku::isContradiction(int row, int col)
    {
        for (int digit: digits)
        {

        }
    }

    vector<int> Sudoku::find_empty()
    {
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                if (grid[i][j] == -1)
                {
                    return {i, j};
                }
            }
        }

        return {0, 0};
    }

    vector<Grid> Sudoku::solve()
    {
        vector<Grid> result = vector<Grid>();

        if (solved())
        {
            Grid solved = Grid(grid, digits);
            result.push_back(solved);
        }

        else 
        {
            vector<int> coordinates = find_empty();
            if (isContradiction(coordinates[0], coordinates[1]))
            {
                return {};
            }

            else 
            {
                for (int num: digits)
                {
                    if (canPlace(coordinates[0], coordinates[1], num))
                    {
                        grid[coordinates[0]][coordinates[1]] = num;
                        result.reserve(result.size() + distance(solve().begin(), solve().end()));
                        result.insert(result.end(), solve().begin(), solve().end());
                        grid[coordinates[0]][coordinates[1]] = -1;
                        // copy(solve().begin(), solve().end(), back_inserter(result));
                    }
                }
            }
        }

        return result;
    }

};

// complete solve and the other things before doing other parts of this project

class Grid 
{
    public: 
        vector<int> digits;
        vector<vector<int>> grid;

    Grid(vector<vector<int>> _grid, vector<int> _digits)
    {
        grid = _grid;
        digits = _digits;
    }

    string Grid::toString()
    {
        return "";
    }

    vector<vector<int>> Grid::grid()
    {
        return grid;
    }

};

int main()
{
    // Do something in this program
}