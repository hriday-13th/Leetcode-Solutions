class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        
        for i in roads:
            degree[i[0]] += 1
            degree[i[1]] += 1
        
        degree.sort(reverse=True)
        
        res = 0
        
        for i, ele in enumerate(degree):
            res += (n - i) * ele
            
        return res