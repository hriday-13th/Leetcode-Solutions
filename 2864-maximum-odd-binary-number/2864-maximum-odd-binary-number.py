class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cone = s.count("1")
        czero = s.count("0")
        
        return "1" * (cone - 1) + "0" * czero + "1"