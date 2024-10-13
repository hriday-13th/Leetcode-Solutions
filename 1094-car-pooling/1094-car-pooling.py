class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sets = []
        
        for people, src, dest in trips:
            sets.append((src, people))
            sets.append((dest, -people))
            
        sets.sort()
        
        curr_passengers = 0
        
        for pt, people in sets:
            curr_passengers += people
            if curr_passengers > capacity:
                return False
                
        return True