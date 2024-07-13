class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [[positions[i], healths[i], directions[i], i] for i in range(n)]
        robots.sort()
        
        stack = []
        
        for r in robots:
            if r[2] == "R" or not stack or stack[-1][2] == "L":
                stack.append(r)
                continue
                
            if r[2] == "L":
                add = True
                while stack and stack[-1][2] == "R" and add:
                    prev = stack[-1][1]
                    if r[1] > prev:
                        stack.pop()
                        r[1] -= 1
                    elif r[1] < prev:
                        stack[-1][1] -= 1
                        add = False
                    else:
                        stack.pop()
                        add = False
            
            if add:
                stack.append(r)
                
        l = sorted(stack, key=lambda x : x[3])
        return [i[1] for i in l]