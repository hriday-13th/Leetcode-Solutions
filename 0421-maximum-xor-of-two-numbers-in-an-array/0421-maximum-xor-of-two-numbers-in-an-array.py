class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, num):
        node = self.root
        
        p = pow(2, 31)
        for _ in range(32):
            if (num & p) > 0:
                if node.one is None:
                    node.one = TrieNode()
                node = node.one
            else:
                if node.zero is None:
                    node.zero = TrieNode()
                node = node.zero
            p //= 2
            
    def findMax(self, num):
        node = self.root
        ans = 0
        
        p = pow(2, 31)
        for _ in range(32):
            if num & p > 0:
                if node.zero is not None:
                    node = node.zero
                else:
                    node = node.one
                    ans += p
            else:
                if node.one is not None:
                    node = node.one
                    ans += p
                else:
                    node = node.zero
            p //= 2
            
        return ans ^ num

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        res = 0
        
        for x in nums:
            trie.add(x)
            res = max(res, trie.findMax(x))
        
        return res