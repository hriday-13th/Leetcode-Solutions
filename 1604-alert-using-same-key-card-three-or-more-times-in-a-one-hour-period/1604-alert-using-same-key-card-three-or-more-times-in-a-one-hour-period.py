class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        tracker = defaultdict(list)
        res = set()
        
        for i in range(len(keyName)):
            h, m = [int(i) for i in keyTime[i].split(":")]
            t = h * 60 + m
            tracker[keyName[i]].append(t)
            
        for n in tracker:
            times = sorted(tracker[n])
            for i in range(2, len(times)):
                if times[i] - times[i - 2] < 61:
                    res.add(n)
                    break
                    
        return sorted(res)