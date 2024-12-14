class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_instance = defaultdict(int)
        n = len(s)
        
        for i in range(n):
            last_instance[s[i]] = i
            
        res = []
        l, r = 0, 0
        
        while r < n:
            curr_limit = last_instance[s[r]]
            while r < curr_limit:
                r += 1
                curr_limit = max(curr_limit, last_instance[s[r]])
            res.append(r - l + 1)
            r += 1
            l = r
            
        return res