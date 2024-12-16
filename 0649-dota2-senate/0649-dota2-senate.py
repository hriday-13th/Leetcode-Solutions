class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = Counter(senate)
        
        q = deque()
        for s in senate:
            q.append(s)
            
        r_count, d_count = 0, 0
        
        while q:
            if senators['R'] == 0 or senators['D'] == 0:
                break
            senator = q.popleft()
            if senator == 'R':
                if r_count > 0:
                    r_count -= 1
                    senators[senator] -= 1
                else:
                    d_count += 1
                    q.append(senator)
            else:
                if d_count > 0:
                    d_count -= 1
                    senators[senator] -= 1
                else:
                    r_count += 1
                    q.append(senator)
                    
        if senators['R'] == 0:
            return 'Dire'
        else:
            return 'Radiant'