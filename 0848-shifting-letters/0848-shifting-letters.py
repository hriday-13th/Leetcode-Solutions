class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        
        prefix = []
        
        for i in shifts[::-1]:
            if prefix == []:
                prefix.append(i)
            else:
                prefix.append(i + prefix[-1])
                
        prefix = prefix[::-1]
        
        for i in range(len(prefix)):
            t = (ord(s[i]) - ord('a') + prefix[i]) % 26
            s = s[:i] + chr(ord('a') + t) + s[i+1:]
            
        return s