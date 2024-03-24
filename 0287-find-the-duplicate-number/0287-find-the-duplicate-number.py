class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            correct = arr[i] - 1
            if arr[i] != arr[correct]:
                arr[i], arr[correct] = arr[correct], arr[i]
            else:
                i += 1
        
        for i in range(len(arr)):
            if arr[i] != i + 1:
                return arr[i]
#         s = sorted(nums)
        
#         for i in range(1, len(s)):
#             if s[i] == s[i-1]:
#                 return s[i]