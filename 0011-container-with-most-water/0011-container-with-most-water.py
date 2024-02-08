class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i, j = 0, len(h) - 1
        
        while (i < j):
            if h[i] < h[j]:
                temp = (j-i) * h[i]
                if temp > max_area:
                    max_area = temp
                i += 1
            else:
                temp = (j-i) * h[j]
                if temp > max_area:
                    max_area = temp
                j -= 1
                
        return max_area