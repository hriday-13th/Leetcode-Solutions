class Solution:  
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr, k):
            l, h = 0, len(arr)-1
            while l <= h:
                m = (l+h) // 2
                if arr[m] == k:
                    return True
                elif arr[m] < k:
                    l = m + 1
                elif arr[m] > k:
                    h = m - 1
            return False
                    
        for row in matrix:
            if row and row[0] <= target <= row[-1]:
                if search(row, target): return True
        
        return False