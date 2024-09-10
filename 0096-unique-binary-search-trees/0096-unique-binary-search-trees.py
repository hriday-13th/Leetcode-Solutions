class Solution:
    memo = {0 : 1, 1 : 1}
    def numTrees(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        count = 0
        
        for i in range(1, n + 1):
            left = self.numTrees(i - 1)
            right = self.numTrees(n - i)
            count += left * right
            
        self.memo[n] = count
        return self.memo[n]