from sortedcontainers import SortedDict
class Solution:
    def isNStraightHand(self, hand: List[int], group: int) -> bool:
        n = len(hand)
        if group == 1 and n > 0:
            return True
        
        if n % group != 0:
            return False
        
        count = SortedDict(Counter(hand))
        grp = n // group
        
        for _ in range(grp):
            curr = list(count.keys())[0]
            for i in range(group):
                if curr in count:
                    count[curr] -= 1
                    if count[curr] == 0:
                        count.pop(curr)
                else:
                    return False
                curr += 1
                
        return True