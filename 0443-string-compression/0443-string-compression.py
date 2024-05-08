class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return len(chars)
        
        last = 0
        i = 0
        
        while i < len(chars):
            st = chars[i]
            freq = 0
            while i < len(chars) and chars[i] == st:
                freq += 1
                i += 1
            chars[last] = st
            last += 1
            if freq > 1:
                add = str(freq)
                for ele in add:
                    chars[last] = ele
                    last += 1
            
        return last