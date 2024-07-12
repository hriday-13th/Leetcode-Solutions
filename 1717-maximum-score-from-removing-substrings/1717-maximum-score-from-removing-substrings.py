class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pat1, pat1_score = ("ab", x) if x >= y else ("ba", y)
        pat2, pat2_score = ("ba", y) if pat1 == "ab" else ("ab", x)
        
        def calc(s, pat, pat_score):
            stack = []
            res = 0
            
            for i in s:
                if stack and stack[-1] == pat[0] and i == pat[1]:
                    res += pat_score
                    stack.pop()
                else:
                    stack.append(i)
                    
            return "".join(stack), res
        
        remaining, score1 = calc(s, pat1, pat1_score)
        rem2, score2 = calc(remaining, pat2, pat2_score)
        
        return score1 + score2