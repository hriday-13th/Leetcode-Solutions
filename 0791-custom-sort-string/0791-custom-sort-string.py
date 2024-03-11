class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # d = {ele: order.index(ele) if ele in order else float('inf') for ele in s}
        l = [order.index(ele) if ele in order else float('inf') for ele in s]
        
        tup = [(s[i], l[i]) for i in range(len(s))]
        
        sor = sorted(tup, key=lambda x:x[1])
        
        res = ''.join(i[0] for i in sor)
        
        return res