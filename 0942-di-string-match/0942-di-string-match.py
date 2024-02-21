class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = list(range(0,len(s)+1))
        res = []
        for i in s:
            if i == "I":
                m = l.pop(0)
                res.append(m)
            elif i == "D":
                t = l.pop(-1)
                res.append(t)
        res.append(l[0])
        return res