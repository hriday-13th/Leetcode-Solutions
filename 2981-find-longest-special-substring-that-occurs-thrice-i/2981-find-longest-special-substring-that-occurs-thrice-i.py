from sortedcontainers import SortedDict
class Solution:
    def maximumLength(self, s: str) -> int:
        dic = {chr(ord('a') + i) : SortedDict() for i in range(26)}
        
        curr_chr = None
        curr_freq = 0
        
        for i in s:
            if curr_chr is None or i != curr_chr:
                if curr_chr is not None:
                    dic[curr_chr][curr_freq] = dic[curr_chr].get(curr_freq, 0) + 1
                curr_chr = i
                curr_freq = 1
            else:
                curr_freq += 1
        
        if curr_chr is not None:
            dic[curr_chr][curr_freq] = dic[curr_chr].get(curr_freq, 0) + 1
            
        ans = -1
        place = -1
        for i in dic:
            prev = 0
            for freq in dic[i]:
                if freq > prev:
                    if prev != 0:
                        ans = max(ans, prev)
                    prev = freq
                if dic[i][freq] == 2 and freq > 2:
                    ans = max(ans, freq - 1)
                elif dic[i][freq] >= 3:
                    ans = max(ans, freq)
                elif freq > 2:
                    ans = max(ans, freq - 2)
                    
        return ans