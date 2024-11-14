class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        n = len(num)
        odd, even = [], []
        
        arr = [int(i) for i in num]
        
        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
                
        odd.sort()
        even.sort()
        res = 0
        
        for i in range(n):
            if arr[i] % 2 == 0:
                res = res * 10 + even.pop()
            else:
                res = res * 10 + odd.pop()
            
        return res