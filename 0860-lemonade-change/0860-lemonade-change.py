class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {i : 0 for i in [5, 10]}
        
        for i in bills:
            if i == 5:
                change[i] += 1
            elif i == 10:
                change[i] += 1
                if change[5] < 1:
                    return False
                else:
                    change[5] -= 1
            elif i == 20:
                if change[10] < 1:
                    if change[5] < 3:
                        return False
                    else:
                        change[5] -= 3
                else:
                    if change[5] < 1:
                        return False
                    else:
                        change[10] -= 1
                        change[5] -= 1
                        
        return True