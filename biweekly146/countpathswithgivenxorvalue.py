# You are given a 2D integer array grid with size m x n. You are also given an integer k.

# Your task is to calculate the number of paths you can take from the top-left cell (0, 0) 
# to the bottom-right cell (m - 1, n - 1) satisfying the following constraints:

# You can either move to the right or down. Formally, from the cell (i, j) you may move to the cell 
# (i, j + 1) or to the cell (i + 1, j) if the target cell exists.
# The XOR of all the numbers on the path must be equal to k.
# Return the total number of such paths.

# Since the answer can be very large, return the result modulo 109 + 7.

class Solution:
    def countPathsWithXorValue(self, grid, k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        res = []
        
        def dfs(r, c, cur_xor):
            if r == rows or c == cols:
                return
            if (r, c) == (rows-1,cols-1) and cur_xor == k:
                res.append(0)
                return

            if r+1 < rows:
                one = cur_xor ^ grid[r+1][c]
                dfs(r+1, c, one)
            if c+1 < cols:
                two = cur_xor ^ grid[r][c+1]
                dfs(r, c+1, two)

        dfs(0, 0, grid[0][0])
        return len(res)