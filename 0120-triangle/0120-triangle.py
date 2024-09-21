class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        curr_len = len(triangle[-1])
        curr_row = curr_len - 2
        
        while curr_row > -1:
            for i in range(curr_len - 1):
                triangle[curr_row][i] += min(triangle[curr_row + 1][i], triangle[curr_row + 1][i+1])
            curr_len -= 1
            curr_row -= 1
        
        return triangle[0][0]