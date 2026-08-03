class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        def get_value(i: int) -> int:
            return matrix[i // n][i % n]
        
        left = 0
        right = m * n

        while left < right:
            midpoint = (left + right) // 2
            if get_value(midpoint) < target:
                left = midpoint + 1
            else: #get_value(midpoint) >= target
                right = midpoint
        
        # If the target is greater than all nums in Matrix, then right will be > m*n
        # so return False. Otherwise, target is within the range of the matrix
        # so check if it was found and return True/False
        return False if right >= m*n else get_value(right) == target