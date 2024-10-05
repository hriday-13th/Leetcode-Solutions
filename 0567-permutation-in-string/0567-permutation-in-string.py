class Solution(object):
    def checkInclusion(self, s1, s2):
        m, n = len(s1), len(s2)
        s1_count, s2_count = [0] * 26, [0] * 26
        
        if m > n:
            return False
        
        for i in range(m):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        if s1_count == s2_count:
            return True
        
        for i in range(m, n):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - m]) - ord('a')] -= 1
            
            if s1_count == s2_count:
                return True
            
        return False