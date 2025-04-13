#pragma once

class Sudoku
{
    private:
        bool solved();
        bool has_digit();
        bool check_square();
        bool check_row_col();
        bool canPlace();
        bool isContradiction();

    public:
        string toString();
        vector<int> find_empty();
    


};