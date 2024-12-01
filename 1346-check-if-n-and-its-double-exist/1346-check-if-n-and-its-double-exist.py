class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        
        for i in arr:
            is_even = i % 2 == 0
            if 2 * i in seen or (is_even and i // 2 in seen):
                return True
            seen.add(i)
            
        return False