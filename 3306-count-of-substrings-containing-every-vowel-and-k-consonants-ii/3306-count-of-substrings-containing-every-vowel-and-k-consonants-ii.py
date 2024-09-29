class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        cons_count = 0
        
        vowels = "aeiou"
        d = defaultdict(int)
        
        l_left, l_right = 0, 0
        res = 0
        
        for r in range(n):
            if word[r] in vowels:
                d[word[r]] += 1
            else:
                cons_count += 1
                
            while cons_count > k and l_right < r:
                if word[l_right] in vowels:
                    d[word[l_right]] -= 1
                    if d[word[l_right]] == 0:
                        del d[word[l_right]]
                else:
                    cons_count -= 1
                l_right += 1
                l_left = l_right
                
            while cons_count == k and l_right < r:
                if word[l_right] in vowels:
                    if d[word[l_right]] - 1 > 0:
                        d[word[l_right]] -= 1
                        l_right += 1
                    else:
                        break
                else:
                    break
                    
            if cons_count == k and len(d) == 5:
                res += (l_right - l_left + 1)
        
        return res