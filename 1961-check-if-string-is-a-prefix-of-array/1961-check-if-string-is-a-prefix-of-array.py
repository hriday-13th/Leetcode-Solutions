class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in words:
            if s == "":
                return True
            if not s.startswith(i):
                return False
            s = s[len(i):]
            
        return s == ""