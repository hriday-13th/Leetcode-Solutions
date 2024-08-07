class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        messages, count = 1, 1
        
        while messages * (3 + len(str(messages))) + count + len(message) > messages * limit:
            if 3 + len(str(messages)) * 2 >= limit:
                return []
            messages += 1
            count += len(str(messages))
            
        ans = []
        
        for i in range(1, messages + 1):
            lim = limit - 3 - len(str(messages)) - len(str(i))
            s, message = message[:lim], message[lim:]
            ans.append(f"{s}<{i}/{messages}>")
            
        return ans