class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def cal(ind, l):
            if ind == len(digits):
                res.append("".join(l))
                return 
            
            for ele in mappings[digits[ind]]:
                l.append(ele)
                cal(ind + 1, l)
                l.pop()
                
        res = []
        cal(0, [])
        return res