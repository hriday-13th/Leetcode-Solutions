class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = [[] for _ in range(n)]
        
        sums[0].append(nums[0])
        
        for i in range(1, n):
            sums[i].append(nums[i])
            for ele in sums[i-1]:
                sums[i].append(ele + nums[i])
                
        new_lis = [i for j in sums for i in j]
        new_lis.sort()
        
        return sum(new_lis[left - 1 : right]) % 1000000007