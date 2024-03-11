class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = {}
        
        def cal(i):
            if i in memo:
                return memo[i]
            
            if i == 1:
                return {"()"}
            
            lis = set()
            
            for k in cal(i-1):
                for j in range(-2, 2*n, 2):
                    add = "(" + k[:j] + ")" + k[j:]
                    lis.update([add])
                # add1 = "(" + k + ")"
                # add2 = k + "()"
                # add3 = "()" + k
                # lis.update([add1, add2, add3])
                
            memo[i] = lis
            return memo[i]
        
        return list(cal(n))
        