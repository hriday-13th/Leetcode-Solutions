class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        l, acts = list(range(1,n+1)), []
        
        for i in l:
            if (i == target[-1]):
                acts += ["Push"]
                return acts
            else:
                if i in target:
                    acts += ["Push"]
                else:
                    acts += ["Push", "Pop"]
                