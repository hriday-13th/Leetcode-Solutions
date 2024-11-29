class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        seen = set()
        
        for i in c:
            if c[i] in seen:
                return False
            else:
                seen.add(c[i])
                
        return True