class Solution:
    def minMutation(self, s: str, e: str, bank: List[str]) -> int:
        def checker(a, b):
            return sum(1 for i in range(8) if a[i] != b[i]) == 1
        
        q = deque([s])
        visited = set(s)
        res = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == e:
                    return res
                for nbr in bank:
                    if checker(nbr, curr) and nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
            res += 1
        
        return -1