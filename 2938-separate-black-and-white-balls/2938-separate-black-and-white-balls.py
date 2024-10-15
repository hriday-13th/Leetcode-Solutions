class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        count_zero = 0
        
        for i in s[::-1]:
            if i == "0":
                count_zero += 1
            else:
                count += count_zero
        
        return count