class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            
            visit.add(src)
            path.add(src)
            for n in adj[src]:
                if not dfs(n, adj, visit, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True
        
        def topology(arr):
            adj = defaultdict(list)
            for src, dest in arr:
                adj[src].append(dest)
                
            visit, path = set(), set()
            order = []
            
            for src in range(1, k + 1):
                if not dfs(src, adj, visit, path, order):
                    return []
            return order[::-1]
            
        row_order = topology(rowConditions)
        col_order = topology(colConditions)
        
        if not row_order or not col_order:
            return []
        
        rows = {num : i for i, num in enumerate(row_order)}
        cols = {num : i for i, num in enumerate(col_order)}
        
        res = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            r, c = rows[num], cols[num]
            res[r][c] = num
            
        return res