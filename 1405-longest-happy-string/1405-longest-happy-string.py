class Solution(object):
    def longestDiverseString(self, a, b, c):
        max_heap = []
    
        if a > 0:
            heapq.heappush(max_heap, (-a, "a"))
        if b > 0:
            heapq.heappush(max_heap, (-b, "b"))
        if c > 0:
            heapq.heappush(max_heap, (-c, "c"))

        res = ""

        while max_heap:
            count1, char1 = heapq.heappop(max_heap)

            if len(res) > 1 and res[-2] == res[-1] == char1:
                if not max_heap:
                    return res
                count2, char2 = heapq.heappop(max_heap)
                res += char2
                count2 += 1
                if count2 < 0:
                    heapq.heappush(max_heap, (count2, char2))
                heapq.heappush(max_heap, (count1, char1))
                continue

            res += char1
            count1 += 1
            if count1 < 0:
                heapq.heappush(max_heap, (count1, char1))

        return res