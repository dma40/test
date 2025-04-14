using namespace std;

#include <vector>
#include "Grid.h"

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

        string toString()
        {
            return "";
        }

        vector<vector<int>> grid()
        {
            return grid;
        }

};