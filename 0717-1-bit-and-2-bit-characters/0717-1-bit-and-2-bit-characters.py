class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        s = "".join([str(b) for b in bits])
        
        i = 0
        
        while i < len(s):
            if s[i] == "0" and i == len(s) - 1:
                return True
            elif s[i] == "1":
                i += 1
            i += 1
            
        return False