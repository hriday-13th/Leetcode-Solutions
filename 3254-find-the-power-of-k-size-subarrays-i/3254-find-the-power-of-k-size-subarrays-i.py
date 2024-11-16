class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        def check(ind):
            c = nums[ind]
            for i in range(ind, ind + k):
                if nums[i] != c:
                    return False
                c += 1
            return True
        
        res = []
        is_prev = False
        prev = -1
        
        for i in range(len(nums) - k + 1):
            if is_prev:
                if nums[i + k - 1] != nums[prev] + k:
                    is_prev = False
            else:
                is_prev = check(i)
            prev += 1
            val = max(nums[i : i + k]) if is_prev else -1
            res.append(val)
            
        return res