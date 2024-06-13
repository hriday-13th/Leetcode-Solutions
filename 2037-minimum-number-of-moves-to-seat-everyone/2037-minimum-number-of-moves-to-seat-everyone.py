class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        s1 = sorted(seats)
        s2 = sorted(students)
        
        cnt = 0
        
        for a, b in zip(s1, s2):
            cnt += abs(b-a)
            
        return cnt