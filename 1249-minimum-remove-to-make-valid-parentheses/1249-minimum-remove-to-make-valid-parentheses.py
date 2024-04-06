class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0
        
        for ele in s:
            if ele == "(":
                res.append(ele)
                count += 1
            elif ele == ")" and count > 0:
                res.append(ele)
                count -= 1
            elif ele != ")":
                res.append(ele)
                
        ans = []
        
        for i in res[::-1]:
            if i == "(" and count > 0:
                count -= 1
            else:
                ans.append(i)
                
        return ''.join(ans[::-1])