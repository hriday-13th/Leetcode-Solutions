class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anag = {}
        
        for i in strs:
            s = ''.join(sorted(i))
            if s in anag:
                anag[s].append(i)
            else:
                anag[s] = [i]
                
        return anag.values()