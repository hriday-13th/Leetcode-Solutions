class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
#         if left == 0 or right == 0:
#             return 0
        
#         elif left == right:
#             return left
        
#         res = left
#         while res != 0 and left < right:
#             left += 1
#             res ^= left
            
#         return res