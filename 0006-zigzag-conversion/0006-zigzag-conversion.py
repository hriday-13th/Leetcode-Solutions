class Solution:
    def convert(self, s: str, numRows: int) -> str:
        step = 2 * (numRows - 1)
        l = len(s)


        if (step == 0 or step == 1):
            return s
        
        a = [s[x] for x in range(0, l, step)]
        b = [s[x] for x in range(numRows-1, l, step)]
        
        tem = []
        for i in range(1, numRows-1):
            t1 = [s[x] for x in range(i, l, step)]
            t2 = [s[x] for x in range(step-i, l, step)]
            k = [item for pair in zip(t1,t2) for item in pair]
            if len(t1) > len(t2):
                k += [t1[-1]]
            elif len(t1) < len(t2):
                k += [t2[-1]]
            tem += k
            
        j = a + tem + b
        delimiter=''
        return delimiter.join(j)


#         l_zero = [s[x] for x in range(0,l,step)] + [s[1]]
#         l_med = [s[y] for y in range(step//2,l,step)]
#         # if l%step == 0:
#         #     l_med = [s[y] for y in range(step//2,l,step)]
#         # else:
#         #     l_med = [s[-2]] + [s[y] for y in range(step//2,l,step)]
#         l_rest = []
        
#         if numRows % 2 != 0:
#             m = step//2
#         else:
#             m = step//2 + 1
        
#         for i in range(1,m):
#             tem1 = [s[z-i] for z in range(step,l,step)]
#             tem2 = [s[z+i] for z in range(step,l,step)]
            
#             l_rest = [item for pair in zip(tem1, tem2) for item in pair]
        
#         j = l_zero + l_rest + l_med
#         delimiter = ''
#         return delimiter.join(j)
