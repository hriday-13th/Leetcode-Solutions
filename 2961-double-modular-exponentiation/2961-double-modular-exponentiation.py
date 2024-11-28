class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        d = defaultdict(list)
        
        for i, ele in enumerate(variables):
            a, b, c, m = ele
            val = (((a ** b) % 10) ** c) % m
            d[val].append(i)
            
        return d[target] if target in d else []