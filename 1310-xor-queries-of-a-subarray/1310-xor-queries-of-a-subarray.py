class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0] * len(arr)
        pre[0] = arr[0]
        res = []
        
        for i in range(1, len(arr)):
            pre[i] = pre[i-1] ^ arr[i]
            
        for l, r in queries:
            if l == 0:
                res.append(pre[r])
            else:
                res.append(pre[r] ^ pre[l-1])
                
        return res