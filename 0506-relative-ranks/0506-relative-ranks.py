class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = [0] * len(score)
        
        for i in range(len(score)):
            for j in range(len(score)):
                if j != i and score[j] > score[i]:
                    rank[i] += 1
        print(rank)
        for i in range(len(rank)):
            if rank[i] == 0:
                score[i] = "Gold Medal"
                
            elif rank[i] == 1:
                score[i] = "Silver Medal"
                
            elif rank[i] == 2:
                score[i] = "Bronze Medal"
                
            else:
                score[i] = str(rank[i]+1)
                
        return score