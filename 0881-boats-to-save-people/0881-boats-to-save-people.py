class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        res = 0
        
        i, j = 0, len(people) - 1
        
        while i <= j:
            if i == j:
                i += 1
                res += 1
            else:
                if people[i] + people[j] <= limit:
                    i += 1
                    j -= 1
                    res += 1
                else:
                    res += 1
                    j -= 1
                    
        return res