class Solution(object):
    def canChange(self, start, target):
        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        ls = [i for i in range(len(start)) if start[i] == "L"]
        rs = [i for i in range(len(start)) if start[i] == "R"]
        lt = [i for i in range(len(target)) if target[i] == "L"]
        rt = [i for i in range(len(target)) if target[i] == "R"]
        
        for i, j in zip(ls, lt):
            if i < j:
                return False
            
        for i, j in zip(rs, rt):
            if i > j:
                return False
            
        return True