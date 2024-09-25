class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            # node.val += 1
            node = node.children[w]
            node.val += 1
        
    def lookup(self, word):
        node = self.root
        score = 0
        for w in word:
            # score += node.val
            node = node.children[w]
            score += node.val
        return score
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        # print(trie.lookup('a'))
        return [trie.lookup(w) for w in words]