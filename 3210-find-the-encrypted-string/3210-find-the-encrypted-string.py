class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        
        for i in range(len(s)):
            ans += s[(i+k) % n]
            
        return ans