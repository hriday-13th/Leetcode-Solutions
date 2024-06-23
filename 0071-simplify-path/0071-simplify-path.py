class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        
        res = []
        
        for i in l:
            if i != "":
                if i == ".":
                    continue
                if i == "..":
                    if res == []:
                        continue
                    else:
                        res.pop()
                else:
                    res.append("/" + i)
                    
        return ''.join(res) if res != [] else "/"