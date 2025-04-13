using namespace std;

#include <vector>

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