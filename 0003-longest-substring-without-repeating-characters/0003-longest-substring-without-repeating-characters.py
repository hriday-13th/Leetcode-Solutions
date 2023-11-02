class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0):
            return 0
        max = 1
        for i in range(len(s)):
            patt = s[i]
            
            for j in range(i+1, len(s)):
                if s[j] not in patt:
                    patt += s[j]
                else:
                    break

            if (len(patt) > max):
                max = len(patt)
            else:
                continue
        return max