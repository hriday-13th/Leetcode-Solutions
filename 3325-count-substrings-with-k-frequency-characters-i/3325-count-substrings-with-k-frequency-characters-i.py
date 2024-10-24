class Solution(object):
    def numberOfSubstrings(self, s, k):
        cnt = Counter()
        res, l = 0, 0
        
        for c in s:
            cnt[c] += 1
            while cnt[c] >= k:
                cnt[s[l]] -= 1
                l += 1
            res += l
            
        return res