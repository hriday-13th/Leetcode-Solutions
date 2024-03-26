class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = {ele: ind for ind, ele in enumerate(s)}
        st = []
        
        for i, char in enumerate(s):
            if char in st:
                continue
            while st and st[-1] > char and i < d[st[-1]]:
                st.pop()
            st.append(char)
        return ''.join(st)