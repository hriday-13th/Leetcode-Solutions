class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        
        prev = 'a'
        
        for i in word:
            diff = abs(ord(i) - ord(prev))
            res += min(diff, abs(26 - diff))
            res += 1
            prev = i
        
        return res