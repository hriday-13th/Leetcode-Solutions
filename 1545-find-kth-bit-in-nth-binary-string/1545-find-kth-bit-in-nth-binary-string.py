class Solution:
    arr = {0: "0"}
    
    def __init__(self):
        def rev(n):
            res = ""
            for i in n:
                if i == "0":
                    res += "1"
                else:
                    res += "0"
            return res
            
        for i in range(1, 21):
            Solution.arr[i] = Solution.arr[i-1] + "1" + rev(Solution.arr[i-1])[::-1]
    
    def findKthBit(self, n: int, k: int) -> str:
        return Solution.arr[n][k-1]
