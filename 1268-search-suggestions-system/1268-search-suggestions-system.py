class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if node.n < 3:
                node.words.append(word)
                node.n += 1
                
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return ''
            node = node.children[c]
        return node.words

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        trie = Trie()
        for p in products:
            trie.insert(p)
        res = []
        pre = ''
        for c in searchWord:
            pre += c
            res.append(trie.search(pre))
        return res