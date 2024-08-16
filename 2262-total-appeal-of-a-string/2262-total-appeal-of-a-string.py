class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, curr = 0, 0
        prev = defaultdict(lambda: -1)
        
        for i, ch in enumerate(s):
            curr += i - prev[ch]
            prev[ch] = i
            res += curr
            
        return res