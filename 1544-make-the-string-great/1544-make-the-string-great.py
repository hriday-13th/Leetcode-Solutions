class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        st = []
        
        for i in range(len(s)):
            if not st and i < len(s):
                st.append(s[i])
            elif abs(ord(st[-1]) - ord(s[i])) == 32:
                st.pop(-1)
            else:
                st.append(s[i])
                
        return ''.join(st)