class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary(potions, spell, target):
            l, r = 0, len(potions)
            while l < r:
                mid = l + (r - l) // 2
                if potions[mid] * spell >= target:
                    r = mid
                else:
                    l = mid + 1
            return len(potions) - l
        
        potions.sort()
        res = []
        for spell in spells:
            res.append(binary(potions, spell, success))
            
        return res