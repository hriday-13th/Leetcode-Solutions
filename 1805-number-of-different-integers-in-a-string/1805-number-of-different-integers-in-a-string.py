class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        
        size = 0
        
        for i in range(len(word)):
            if word[i].isnumeric():
                size += 1
            else:
                if size > 0:
                    nums.add(int(word[i - size: i]))
                    size = 0
                    
        if size > 0:
            nums.add(int(word[-size:]))
            
        return len(nums)