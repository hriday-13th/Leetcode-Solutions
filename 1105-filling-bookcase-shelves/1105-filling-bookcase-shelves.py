class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        min_height = [float('inf')] * (n+1)
        min_height[0] = 0
        
        for i in range(1, n+1):
            currWidth = 0
            currHeight = 0
            
            for j in range(i-1, -1, -1):
                if currWidth + books[j][0] > shelfWidth:
                    break
                currHeight = max(currHeight, books[j][1])
                currWidth += books[j][0]
                
                possibleHeight = min_height[j] + currHeight
                
                min_height[i] = min(min_height[i], possibleHeight)
                
        return min_height[n]