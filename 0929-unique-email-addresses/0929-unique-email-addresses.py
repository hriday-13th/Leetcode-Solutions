class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        copy = set()
        
        for i in emails:
            pre, dom = i.split("@")
            pre = pre.split("+")[0].replace(".","")
            copy.add(pre + "@" + dom)
        
        return len(copy)