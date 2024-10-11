class Solution(object):
    def smallestChair(self, times, targetFriend):
        n = len(times)
        order = sorted(range(n), key=lambda x: times[x][0])
        emptyseats, takenseats = list(range(n)), []
        
        for i in order:
            arr, lev = times[i]
            
            while takenseats and takenseats[0][0] <= arr:
                heappush(emptyseats, heappop(takenseats)[1])
                
            seat = heappop(emptyseats)
            
            if i == targetFriend:
                return seat
            
            heappush(takenseats, (lev, seat))