class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        
        for i in bank:
            count = i.count("1")
            if count == 0:
                continue
            else:
                res += prev * count
            prev = count
            
        return res