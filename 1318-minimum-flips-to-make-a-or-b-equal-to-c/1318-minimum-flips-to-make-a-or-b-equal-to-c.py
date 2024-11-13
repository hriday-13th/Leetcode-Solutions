class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bits = [0] * 32

        def filler(num):
            for i in range(32):
                if num & (1 << i) != 0:
                    bits[i] += 1

        def negator(num):
            for i in range(32):
                if num & (1 << i) != 0:
                    if bits[i] > 0:
                        bits[i] = 0
                    else:
                        bits[i] = 1

        filler(a)
        filler(b)
        negator(c)

        return sum(abs(i) for i in bits)
