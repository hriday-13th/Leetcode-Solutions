class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        
        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count += 1
        return count