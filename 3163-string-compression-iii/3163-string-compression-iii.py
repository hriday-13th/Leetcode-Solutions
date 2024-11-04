class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        curr_count = 0
        prev = None
        
        for i in word:
            if curr_count == 0:
                curr_count += 1
                prev = i
                continue
            elif i == prev and curr_count < 9:
                curr_count += 1
            else:
                res += str(curr_count) + prev
                curr_count = 1
                prev = i
                
        if curr_count > 0:
            res += str(curr_count) + prev
            
        return res