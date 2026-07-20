class Solution:
    '''
    1-based _get_row helper method
    '''
    def _get_row(self, board, row_number) -> List[str]:
        return board[row_number - 1]
    
    '''
    1-based _get_col helper method
    '''
    def _get_col(self, board, col_number) -> List[str]:
        return [board[row - 1][col_number - 1] for row in [1,2,3,4,5,6,7,8,9]]

    '''
    1-based _get_col helper method
    '''
    def _get_box(self, board, box_number) -> List[str]:
        import math, itertools
        box_row = math.ceil(box_number / 3) #box 1,2,3 is row 1, box 4,5,6 is row 2
        box_col = ((box_number - 1) % 3) #box 1,4,7 is col 1, box 2,5,8 is col 2, box 3,6,9 is col 3
        rows_in_box = range(1,10)[3 * (box_row - 1):3 * (box_row - 1) + 3:]
        cols_in_box = range(1,10)[box_col * 3: box_col * 3 + 3]
        cells_to_check = list(itertools.product(rows_in_box, cols_in_box))
        values = list([board[row - 1][col - 1] for row, col in cells_to_check])
        return values

    '''
    Given an array of 9 values, check if sudoku conditions are true
        - values are 1-9
        - only allowed duplicate is '.'
    '''
    def _is_valid(self, values: List[str]) -> bool:
        numbers = [val for val in values if val != '.']
        return len(numbers) == len(set(numbers))
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_rows_valid = all(map(self._is_valid, board))
        is_cols_valid = all(map(self._is_valid, 
            [self._get_col(board, col) for col in range(1,10)]))
        is_boxes_valid = all(map(self._is_valid, 
            [self._get_box(board, box_num) for box_num in range(1,10)]))
        return is_rows_valid and is_cols_valid and is_boxes_valid