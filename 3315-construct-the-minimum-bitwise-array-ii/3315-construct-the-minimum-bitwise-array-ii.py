class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        def helper(i):
            count = 0
            while i & 1 == 1:
                count += 1
                i >>= 1
            count -= 1
            num = ""
            if i > 0:
                num += str(bin(i)[2:])
            num += "0" + "1" * count
            return int(num, 2)
        
        for i in nums:
            if i == 2:
                ans.append(-1)
            else:
                ans.append(helper(i))
                
        return ans