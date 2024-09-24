class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = defaultdict(lambda: [0] * len(votes[0]))
        
        for vote in votes:
            for i, c in enumerate(vote):
                d[c][i] += 1
                
        sorted_d = sorted(d.keys(), key=lambda t: (d[t], -ord(t)), reverse = True)
        
        return "".join(sorted_d)