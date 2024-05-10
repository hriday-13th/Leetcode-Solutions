class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        rats = []
        
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                t = rats.append([arr[i], arr[j]])
                
        rats = sorted(rats, key=lambda x : x[0] / x[1])
        
        return rats[k-1]