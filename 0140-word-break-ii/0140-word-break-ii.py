class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = [[] for _ in range(n + 1)]
        res[0] = [""]
        
        for i in range(n):
            if res[i]:
                for word in wordDict:
                    if s[i:].startswith(word):
                        for pre in res[i]:
                            res[i + len(word)].append((pre + ' ' + word).strip())
                            
        return res[n]