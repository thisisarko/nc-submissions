class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        l, r = 0, (num_rows * num_cols) - 1

        while l <= r:
            mid = l + (r-l) // 2
            m = mid // num_cols
            n = mid % num_cols
            elem = matrix[m][n]
            if elem == target: return True
            if elem > target: r = mid - 1
            if elem < target: l = mid + 1
        return False