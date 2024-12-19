class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        indices_seen = set()
        nums_seen = set()
        
        for i, num in enumerate(arr):
            indices_seen.add(i)
            nums_seen.add(num)
            
            if indices_seen == nums_seen:
                chunks += 1
                indices_seen = set()
                nums_seen = set()
                
        return chunks