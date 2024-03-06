class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        fuel = 0
        start = 0
        
        for i in range(2*n):
            val = i % n
            fuel += gas[val] - cost[val]
            
            if fuel < 0:
                start = i + 1
                fuel = 0
                
            if i - start == n:
                return start
        return -1
#         i = 0
#         n = len(gas)
        
#         while i < len(gas):
#             flag = True
#             fuel = gas[i]
#             for j in range(i, n + i):
#                 if fuel - cost[j % n] < 0:
#                     flag = False
#                     break
#                 else:
#                     fuel += (gas[(j+1)%n] - cost[j%n])
#             if flag:
#                 return i
#             i += 1
#         return -1