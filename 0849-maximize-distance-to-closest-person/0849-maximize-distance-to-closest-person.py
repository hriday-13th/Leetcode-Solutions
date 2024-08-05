class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = -1
        i = 0
        max_len = -1
        
        while i < len(seats):
            if seats[i] != 1:
                i += 1
            else:
                if prev == -1:
                    max_len = max(max_len, i)
                if (i - prev) // 2 > max_len:
                    max_len = (i - prev) // 2
                prev = i
                i += 1
                
                
        return max(max_len, len(seats) - prev - 1)