class Solution(object):
    def splitMessage(self, message, limit):
        """
        :type message: str
        :type limit: int
        :rtype: List[str]
        """
        no_messages, count = 1, 1
        
        while no_messages * (3 + len(str(no_messages))) + count + len(message) > no_messages * limit:
            if 3 + len(str(no_messages)) * 2 >= limit:
                return []
            no_messages += 1
            count += len(str(no_messages))
            
        ans = []
        
        for i in range(1, no_messages + 1):
            lim = limit - 3 - len(str(i)) - len(str(no_messages))
            s, message = message[:lim], message[lim:]
            temp = s + "<" + str(i) + "/" + str(no_messages) + ">"
            ans.append(temp)
            
        return ans