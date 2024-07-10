class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in magazine:
            ransomNote = ransomNote.replace(i, '', 1)
            
        return ransomNote == ""
                