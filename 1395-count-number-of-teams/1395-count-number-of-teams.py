class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for i in range(n):
            left_low, left_great, right_low, right_great = 0, 0, 0, 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    left_low += 1
                if rating[j] > rating[i]:
                    left_great += 1
                    
            for j in range(i+1, n):
                if rating[j] < rating[i]:
                    right_low += 1
                if rating[j] > rating[i]:
                    right_great += 1
            
            count += left_low * right_great + left_great * right_low
            
        return count