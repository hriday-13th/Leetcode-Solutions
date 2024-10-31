class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        r, f = len(robot), len(factory)
        
        @cache
        def get_min(rindex, findex):
            if rindex == r:
                return 0
            if findex == f:
                return 10 ** 20
            
            x, limit = factory[findex]
            
            best = get_min(rindex, findex + 1)
            cost = 0
            
            for i in range(1, limit + 1):
                if rindex + i > r:
                    break
                    
                cost += abs(x - robot[rindex + i - 1])
                best = min(best, get_min(rindex + i, findex + 1) + cost)
                
            return best
        
        return get_min(0, 0)