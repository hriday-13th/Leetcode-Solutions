class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        num = sorted(deck)
        l = len(num)
        q = [0] * l
        ind = [i for i in range(l)]
        
        for i in range(l):
            if i == l-1:
                continue
            else:
                k = ind.pop(i+1)
                ind.append(k)
                
        for a,b in zip(ind, num):
            q[a] = b
            
        return q