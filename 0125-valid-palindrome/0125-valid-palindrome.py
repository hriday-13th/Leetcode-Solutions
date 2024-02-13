class Solution:
    def isPalindrome(self, s: str) -> bool:
        conv = ""
        for i in s:
            if i.isalnum():
                conv += i
        res = conv.lower()
        
        if res == "" or len(res) == 1:
            return True
        elif res == res[::-1]:
            return True
        else:
            return False