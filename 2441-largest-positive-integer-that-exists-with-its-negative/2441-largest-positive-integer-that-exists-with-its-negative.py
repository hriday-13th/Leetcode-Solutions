class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr = sorted(nums)
        
        i, j = 0, len(arr)-1
        
        while i < j:
            if arr[i] < 0:
                if arr[j] == abs(arr[i]):
                    return arr[j]
                elif arr[j] > abs(arr[i]):
                    j -= 1
                elif arr[j] < abs(arr[i]):
                    i += 1
            else:
                return -1
                
        return -1