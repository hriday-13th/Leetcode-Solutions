class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = [0] * 1001
        uniq = 0
        
        for a, b in zip(target, arr):
            if count[a] == 0:
                uniq += 1
            count[a] += 1
            
            if count[b] == 1:
                uniq -= 1
            count[b] -= 1
            
        return uniq == 0