class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        min_del = 0
        
        for i in s:
            if i == "a":
                min_del = min(min_del + 1, b_count)
            else:
                b_count += 1
                
        return min_del