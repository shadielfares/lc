class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            # Checking if the target is within the current row.
            if matrix[i][0] <= target:
                l, r = 0, len(matrix[i]) - 1
                while l <= r:
                    m = (l+r) // 2
                    if matrix[i][m] > target:
                        r = m - 1
                    elif matrix[i][m] < target:
                        l = m + 1
                    else:
                        return True
        return False
        