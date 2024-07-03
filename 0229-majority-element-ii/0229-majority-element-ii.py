import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, n2 = 0, 1
        count1, count2 = 0, 0
        
        for i in nums:
            if i == n1:
                count1 += 1
            elif i == n2:
                count2 += 1
            elif count1 == 0:
                n1, count1 = i, 1
            elif count2 == 0:
                n2, count2 = i, 1
            else:
                count1 -= 1
                count2 -= 1
                
        count1, count2 = 0, 0
        for num in nums:
            if num == n1:
                count1 += 1
            elif num == n2:
                count2 += 1
                
        res = []
        if count1 > len(nums) // 3:
            res.append(n1)
        if count2 > len(nums) // 3:
            res.append(n2)
            
        return res