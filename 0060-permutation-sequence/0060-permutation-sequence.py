class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perm = []
        count = 0
        
        def finder(perm):
            nonlocal count
            l = len(perm)
            for i in range(1, n + 1):
                if i not in perm:
                    if count + math.factorial(n - l - 1) >= k:
                        return i
                    else:
                        count += math.factorial(n - l - 1)
                        
        while len(perm) < n:
            val = finder(perm)
            perm.append(val)
            
        return "".join([str(i) for i in perm])