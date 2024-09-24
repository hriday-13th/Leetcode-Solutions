class Trie:
    def __init__(self, string):
        self.d = {}
        for ch in string:
            self.add_ele(ch)
            
    def add_ele(self, char):
        d = self.d
        for i in str(char):
            if i not in d:
                d[i] = {}
            d = d[i]
            
    def find_len(self, char):
        d = self.d
        for i, c in enumerate(str(char)):
            if c not in d:
                return i
            d = d[c]
        return i + 1
    
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie(set(arr1))
        
        return max(trie.find_len(ele) for ele in set(arr2))