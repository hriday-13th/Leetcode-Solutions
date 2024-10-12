class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        
        for start, end in intervals:
            events.append((start, 1))
            events.append((end+1, -1))
            
        events.sort()
        
        res = 0
        active = 0
        
        for val, event in events:
            active += event
            res = max(res, active)
            
        return res