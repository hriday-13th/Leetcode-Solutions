class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        def check(a, b):
            return sum(1 for i in range(8) if a[i] != b[i]) == 1
        
        q = deque([startGene])
        visited = set(startGene)
        
        res = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endGene:
                    return res
                for nbr in bank:
                    if check(nbr, curr) and nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
            res += 1
            
        return -1