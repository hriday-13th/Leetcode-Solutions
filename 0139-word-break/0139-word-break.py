class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def cal(t, words):
            if t in memo:
                return memo[t]
            if t == "":
                return True
            
            for w in words:
                if t.startswith(w):
                    suff = t[len(w):]
                    if cal(suff, words):
                        memo[t] = True
                        return memo[t]
                else:
                    continue
                    
            memo[t] = False
            return memo[t]
        
        return cal(s, wordDict)