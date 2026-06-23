class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                k = ((i // 3) * 3) + (j // 3)
                num = board[i][j]
                if num.isdigit():
                    if num in rows[i] or num in cols[j] or num in squares[k]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[k].add(num)

        return True
        