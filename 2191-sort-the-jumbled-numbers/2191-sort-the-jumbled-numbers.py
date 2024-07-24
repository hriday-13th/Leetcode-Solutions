class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums = [str(i) for i in nums]
        num_mapped = []
        
        for idx, ele in enumerate(nums):
            temp = ""
            for c in ele:
                temp += str(mapping[int(c)])
            num_mapped.append([nums[idx], int(temp), idx])
            
        num_mapped.sort(key=lambda item : (item[1], item[2]))
        
        return [int(i[0]) for i in num_mapped]