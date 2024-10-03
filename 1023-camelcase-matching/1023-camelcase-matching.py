class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        
        for word in queries:
            st = list(pattern)
            match = True
            
            for c in word:
                if st and c == st[0]:
                    st.pop(0)
                elif c.isupper():
                    match = False
                    break
                    
            res.append(match and not st)
        
        return res