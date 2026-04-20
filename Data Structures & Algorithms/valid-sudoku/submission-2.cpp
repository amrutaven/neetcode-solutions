class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //three vectors of hash tables
        vector<unordered_map<char, int>> rows_map;
        vector<unordered_map<char, int>> cols_map;
        vector<unordered_map<char, int>> squares_map(9);

        //fill out the rows map
        for (int i = 0; i < 9; i++) {
            unordered_map<char, int> new_map;
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    new_map[board[i][j]]++;
                }
            }
            rows_map.push_back(new_map);
        }

        //fill out the columns map
        for (int i = 0; i < 9; i++) {
            unordered_map<char, int> new_map;
            for (int j = 0; j < 9; j++) {
                if (board[j][i] != '.') {
                    new_map[board[j][i]]++;
                }
            }
            cols_map.push_back(new_map);
        }

        //fill out the squares map
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int index = ((i / 3) * 3) + (j / 3);
                    squares_map[index][board[i][j]]++;
                }
            }
        }

        //now look through the maps for all the numbers in the sudoku
        for (int i = 0; i < 9; i++) {
            for (auto& [key, value] : rows_map[i]) {
                if (value > 1) return false;
            }
            for (auto& [key, value] : cols_map[i]) {
                if (value > 1) return false;
            }
            for (auto& [key, value] : squares_map[i]) {
                if (value > 1) return false;
            }
        }
        return true; 
    }
};
