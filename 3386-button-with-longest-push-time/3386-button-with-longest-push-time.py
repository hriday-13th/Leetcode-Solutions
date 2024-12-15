class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        res = float('inf')
        max_so_far = 0
        prev = 0
        
        for ind, time in events:
            time_to_push = time - prev
            if time_to_push > max_so_far:
                max_so_far = time_to_push
                res = ind
            elif time_to_push == max_so_far:
                res = min(res, ind)
            prev = time
                
        return res