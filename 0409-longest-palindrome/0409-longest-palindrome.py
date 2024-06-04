from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        
        net = 0
        flag = False

        for val in d.values():
            if val % 2 == 0 and val > 0:
                net += val
            elif val % 2 == 1:
                net += val - 1
                flag = True
                
        return net + 1 if flag else net