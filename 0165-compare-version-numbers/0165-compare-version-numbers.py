class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        
        pad = max(len(l1), len(l2))
        l1 += [0] * (pad - len(l1))
        l2 += [0] * (pad - len(l2))
        
        print(l1, l2)
        for a,b in zip(l1,l2):
            a, b = int(a), int(b)
            print(a, b)
            if a > b:
                return 1
            elif a < b:
                return -1
            
        return 0