class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search to find the row that the target is on
        #binary search to find the column it is on

        top = 0
        bottom = len(matrix) - 1 #how many rows there are
        final_row = 0

        while (top <= bottom):

            middle = (bottom + top) // 2

            if matrix[middle][0] <= target <= matrix[middle][-1]:
                final_row = middle
                break
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                bottom = middle - 1
        
        first = 0
        second = len(matrix[0]) - 1

        while (second >= first):
            middle = (second + first) // 2
            if target == matrix[final_row][middle]:
                return True
            if target > matrix[final_row][middle]:
                first = middle + 1
            else:
                second = middle - 1
        
        return False

            


        
        