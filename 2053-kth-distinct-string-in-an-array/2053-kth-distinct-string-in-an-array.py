class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        
        itr = 0
        for i in arr:
            if count[i] == 1:
                itr += 1
            if itr == k:
                return i
            
        return ""