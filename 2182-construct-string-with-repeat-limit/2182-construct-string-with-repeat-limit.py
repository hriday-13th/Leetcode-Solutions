class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = ""
        heap = []
        counter = Counter(s)
        
        for c in counter:
            heapq.heappush(heap, (-ord(c), counter[c]))
            
        while heap:
            order, freq = heapq.heappop(heap)
            char = chr(-order)
            
            while freq > 0:
                if freq > repeatLimit:
                    res += char * repeatLimit
                    
                    if heap:
                        order2, freq2 = heapq.heappop(heap)
                        res += chr(-order2)
                        freq2 -= 1
                        if freq2 > 0:
                            heapq.heappush(heap, (order2, freq2))
                    else:
                        return res
                else:
                    res += char * freq
                freq -= repeatLimit
        
        return res