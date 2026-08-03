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
            if get_value(midpoint) == target:
                return True
            elif get_value(midpoint) < target:
                left = midpoint + 1
            else: #get_value(midpoint) >= target
                right = midpoint
        
        # Target was never found
        return False