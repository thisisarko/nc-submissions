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

        # def get_mid(left, right):
        #     l_m, l_n = left
        #     r_m, r_n = right
        #     delta = ((r_m - l_m) * num_cols) + (r_n - l_n)
        #     delta_mid = delta // 2

        #     mid_m = l_m + (delta_mid // num_cols)
        #     mid_n = 
        
        # def get_next(x):
        #     m, n = x
        #     if n + 1 < num_cols:
        #         return m, n + 1  # same row, next col
        #     if m + 1 < num_rows:
        #         return m + 1, 0  # next row, first col
        #     raise IndexError()

        # def get_prev(x):
        #     m, n = x
        #     if n - 1 >= 0:
        #         return m, n - 1  # same row, prev col
        #     if m - 1 >= 0:
        #         return m - 1, num_cols - 1  # prev row, last col
        #     raise IndexError()

        # def loop_condition(left, right):
        #     l_m, l_n = left
        #     r_m, r_n = right

        #     if l_m < r_m: return True

        #     if (l_m == r_m) and (l_n <= r_n): return True

        #     return False


        # l = (0,0)
        # r = (num_rows - 1, num_cols - 1)

        # while loop_condition(l, r):
        #     mid = (l[0] + r[0]) // 2, (l[1] + r[1]) // 2
        #     mid_elem = matrix[mid[0]][mid[1]]
        #     if mid_elem == target: return True

        #     if mid_elem < target: l = get_next(mid)

        #     if mid_elem > target: r = get_prev(mid)
        
        # return False