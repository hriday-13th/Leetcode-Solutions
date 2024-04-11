class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l = len(num) - k
        if l <= 0:
            return "0"
        
        st = []
        
        for ele in num:
            while k > 0 and st and st[-1] > ele:
                st.pop()
                k -= 1
            st.append(ele)
        
        while k > 0:
            st.pop()
            k -= 1
            
        res = "".join(st[:l]).lstrip("0")
            
        return res if res else '0'