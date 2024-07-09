class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        chef = customers[0][0]
        
        for i in customers:
            if i[0] > chef:
                chef = i[0]
            chef += i[1]
            res += chef - i[0]
            
        return res / len(customers)