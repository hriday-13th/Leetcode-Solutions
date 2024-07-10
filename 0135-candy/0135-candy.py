class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = n
        i = 1
        
        while i < n:
            if ratings[i] == ratings[i-1]:
                print(i)
                i += 1
                continue
                
            peak = 0
            while i < n and ratings[i] > ratings[i-1]:
                print(i)
                peak += 1
                candies += peak
                i += 1
                if candies == n: return candies
                
            dip = 0
            while i < n and ratings[i] < ratings[i-1]:
                print(i)
                dip += 1
                candies += dip
                i += 1
                
            candies -= min(peak, dip)
            
        return candies
#         n = len(ratings)
#         if n == 1:
#             return 1
        
#         candies = [1] * n
        
#         for i in range(1, n):
#             if ratings[i] > ratings[i-1]:
#                 candies[i] = candies[i-1] + 1
                
#         for i in range(n-2, -1, -1):
#             if ratings[i] > ratings[i+1]:
#                 candies[i] = max(candies[i], candies[i+1] + 1)
                
#         return sum(candies)