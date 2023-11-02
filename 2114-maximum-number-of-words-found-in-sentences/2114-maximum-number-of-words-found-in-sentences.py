class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for i in sentences:
            #j = i.split()
            if len(i.split()) > max:
                max = len(i.split())
            else:
                pass

        return max