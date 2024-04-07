class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        @cache
        def foo(i, bal):
            if i == n:
                return bal == 0
            if bal < 0:
                return False
            
            ans = False
            
            if s[i] == "(":
                ans = foo(i+1, bal+1)
            elif s[i] == ")":
                ans = foo(i+1, bal-1)
            else:
                ans = foo(i+1, bal) or foo(i+1, bal+1) or foo(i+1, bal-1)
                
            return ans
        
        return foo(0,0)