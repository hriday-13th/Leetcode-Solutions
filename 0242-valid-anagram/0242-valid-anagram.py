class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tem1 = ''.join(sorted(s))
        tem2 = ''.join(sorted(t))
        
        if tem1 == tem2:
            return True
        else:
            return False