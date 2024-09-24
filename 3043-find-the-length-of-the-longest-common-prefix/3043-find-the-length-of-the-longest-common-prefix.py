class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        seen = set()
        
        for num in arr1:
            while num:
                seen.add(num)
                num //= 10
                
        for num in arr2:
            while num:
                if num in seen:
                    ans = max(ans, num)
                    break
                num //= 10
                
        return len(str(ans)) if ans else 0