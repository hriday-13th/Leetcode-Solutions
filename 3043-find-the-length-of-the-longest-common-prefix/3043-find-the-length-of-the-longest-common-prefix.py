class Trie:
    def __init__(self, nums):
        self.d = {}
        for ele in nums:
            self.add_elem(ele)
    
    def add_elem(self, ele):
        d = self.d
        for char in str(ele):
            if char not in d:
                d[char] = {}
            d = d[char]
            
    def find_len(self, ele):
        d = self.d
        for i, c in enumerate(str(ele)):
            if c not in d:
                return i
            d = d[c]
        return i + 1
        
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie(set(arr1))
        return max(trie.find_len(ele) for ele in set(arr2))