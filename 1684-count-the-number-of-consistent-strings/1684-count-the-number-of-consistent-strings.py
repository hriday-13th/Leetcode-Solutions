class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        s = set(allowed)
        
        for i in words:
            if all(char in s for char in i):
                count += 1
        
        return count