class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid2), len(grid2[0])
        res = 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid2[i][j] != 1:
                return True
            
            is_sub = grid1[i][j] == 1
            
            grid2[i][j] = -1
            
            is_sub &= dfs(i + 1, j)
            is_sub &= dfs(i - 1, j)
            is_sub &= dfs(i, j + 1)
            is_sub &= dfs(i, j - 1)
            
            return is_sub
        
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and dfs(i, j):
                    res += 1
                    
        return res