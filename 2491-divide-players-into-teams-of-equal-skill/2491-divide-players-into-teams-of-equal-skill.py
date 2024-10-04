class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        res, s = 0, 0
        p1, p2 = 0, len(skill) - 1
        
        for i in range(len(skill) // 2):
            if i == 0:
                s = skill[p1] + skill[p2]
                res += skill[p1] * skill[p2]
                
            else:
                if skill[p1] + skill[p2] != s:
                    return -1
                res += skill[p1] * skill[p2]
            p1 += 1
            p2 -= 1
            
        return res