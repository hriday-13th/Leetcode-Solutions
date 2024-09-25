class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word, node = None, index = 0):
        if node == None:
            node = self.root
        if index == len(word):
            return node.is_end
        
        c = word[index]
        if c not in node.children:
            return False
        else:
            return self.search(word, node.children[c], index + 1)

    def startsWith(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)