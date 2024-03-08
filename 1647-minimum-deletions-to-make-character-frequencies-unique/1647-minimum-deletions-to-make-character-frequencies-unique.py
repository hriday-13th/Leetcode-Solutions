class Solution:
    def minDeletions(self, s: str) -> int:
        n = Counter(s)
        rem = 0
        feq = set()
        
        for ch, freq in n.items():
            while freq > 0 and freq in feq:
                freq -= 1
                rem += 1
            feq.add(freq)
        return rem