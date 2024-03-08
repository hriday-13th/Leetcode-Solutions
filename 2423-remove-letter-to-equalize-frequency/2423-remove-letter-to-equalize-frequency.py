class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = {ele: word.count(ele) for ele in set(word)}
        freq = list(d.values())
        
        s = list(set(freq))
        if len(s) == 1:
            return True if (s[0] == 1 or len(freq) == 1) else False
        
        elif len(s) == 2:
            if s[1] - s[0] > 1:
                if s[0] == 1 and freq.count(s[0]) == 1:
                    return True
                else:
                    return False
            else:
                if freq.count(s[0]) > 1 and freq.count(s[1]) > 1:
                    return False
                else:
                    if s[0] >= 1 and freq.count(s[1]) == 1:
                        return True
                    elif s[0] == 1 and freq.count(s[0]) == 1:
                        return True
                    else:
                        return False
        else:
            return False