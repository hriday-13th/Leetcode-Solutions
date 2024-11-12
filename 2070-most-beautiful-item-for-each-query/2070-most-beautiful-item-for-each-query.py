class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        d = defaultdict(int)
        d[-1] = 0
        items.sort()
        prev = 0

        for i, v in items:
            prev = max(prev, v)
            d[i] = prev

        res = []
        search = sorted(d.keys())
        n = len(search)

        def binary(val):
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if search[mid] <= val:
                    l = mid + 1
                else:
                    r = mid - 1
            return search[r] if r >= 0 else -1

        for q in queries:
            key = binary(q)
            res.append(d[key])

        return res