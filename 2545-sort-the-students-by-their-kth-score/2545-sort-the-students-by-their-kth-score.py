class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        order = [score[i][k] for i in range(len(score))]
        
        d = {order[i] : score[i] for i in range(len(score))}
        
        x = dict(sorted(d.items()))
        
        return list(x.values())[::-1]