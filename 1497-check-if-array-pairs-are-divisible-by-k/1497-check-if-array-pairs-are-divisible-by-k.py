class Solution(object):
    def canArrange(self, arr, k):
        rem = [0] * k
        
        for i in arr:
            remainder = i % k
            if remainder < 0:
                remainder += k
            rem[remainder] += 1
            
        if rem[0] % 2 != 0:
            return False
        
        for i in range(1, (k // 2) + 1):
            if rem[i] != rem[k - i]:
                return False
            
        return True