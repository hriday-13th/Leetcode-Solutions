class Solution:
    def minLength(self, s: str) -> int:
        st = []
        
        for i in range(len(s)):
            # print(st)
            if not st:
                st.append(s[i])
            elif (s[i] == "B" and st[-1] == "A") or (s[i] == "D" and st[-1] == "C"):
                st.pop(-1)
            else:
                st.append(s[i])
                
        return len(''.join(st))