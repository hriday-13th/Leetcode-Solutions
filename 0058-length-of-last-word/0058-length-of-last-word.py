class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha():
                count += 1 
            if s[i] == " " and count != 0:
                break
        return count
        # spl = s.split()
        # return len(spl[-1])