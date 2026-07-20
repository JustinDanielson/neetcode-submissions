import itertools
# Elegant Solution
class Solution:
    # Each value in the array is a member of a row, column, and box
    # For each numeric value found, store its value in the row, column, and box
    # If a duplicate value is found, then it is invalid

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: List[int] = [0]*9
        cols: List[int] = [0]*9
        boxs: List[int] = [0]*9
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                value = int(board[row][col])
                box = 3*(row // 3) + (col // 3)
                mask = 0x1 << value
                if rows[row] & mask or \
                    cols[col] & mask or \
                    boxs[box] & mask:
                    return False
                rows[row] = rows[row] | mask
                cols[col] = cols[col] | mask
                boxs[box] = boxs[box] | mask
        return True