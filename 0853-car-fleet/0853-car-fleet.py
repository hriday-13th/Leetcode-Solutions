class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[p, s] for p, s in zip(position, speed)]
        
        st = []
        
        for p, s in sorted(arr)[::-1]:
            time_taken = (target - p) / s
            if len(st) == 0 or st[-1] < time_taken:
                st.append(time_taken)
                
        return len(st)