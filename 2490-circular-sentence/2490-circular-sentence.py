class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lis = sentence.split()
        start = lis[0][0]
        checker = lis[0][-1]
        
        if len(lis) != 1:
            for i in range(1, len(lis)):
                if lis[i][0] != checker:
                    return False
                checker = lis[i][-1]
            
        return checker == start