class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        if ch in word:
            ind = word.index(ch)
            return "".join(word[:ind+1][::-1] + word[ind+1:])
        return "".join(word)