class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = ""
        max_so_far = 0
        prev_time = 0
        
        for i in range(len(releaseTimes)):
            time_taken = releaseTimes[i] - prev_time
            if time_taken > max_so_far:
                res = keysPressed[i]
                max_so_far = time_taken
            elif time_taken == max_so_far:
                res = max(res, keysPressed[i])
            prev_time = releaseTimes[i]
                
        return res