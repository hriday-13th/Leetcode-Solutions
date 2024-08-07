class Solution:
    def numwiz(self, num):
        singles = {"1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}

        teens = {"10":"Ten", "11":"Eleven", "12":"Twelve", "13":"Thirteen", "14":"Fourteen", "15":"Fifteen", "16":"Sixteen", "17":"Seventeen", "18":"Eighteen","19":"Nineteen"}

        tens = {"2":"Twenty", "3":"Thirty", "4":"Forty", "5":"Fifty", "6":"Sixty", "7":"Seventy", "8":"Eighty", "9":"Ninety"}
        
        res = ""
        num = int(num)
        start = True
        if num == 0:
            return "Zero"
        if num > 99:
            digit = num // 100
            res += " " + singles[str(digit)] + " Hundred"
            num %= 100
        if num > 9:
            if num < 20:
                res += " " + teens[str(num)]
                return res[1:]
            digit = num // 10
            res += " " + tens[str(digit)]
            num %= 10
        if num > 0 and num < 10:
            res += " " + singles[str(num)]
                
        return res[1:]
        
    def numberToWords(self, num: int) -> str:
        add_ons = {0:"", 1:"Thousand", 2:"Million", 3:"Billion"}
        res = ""
        num = str(num)[::-1]
        lis = [num[i : i + 3][::-1] for i in range(0, len(num), 3)]
        
        for i in range(len(lis)):
            if len(lis) > 1 and int(lis[0]) == 0 and i == 0:
                continue
            if len(lis) > 2 and int(lis[1]) == 0 and i == 1:
                continue
            if len(lis) > 3 and int(lis[2]) == 0 and i == 2:
                continue
            res = self.numwiz(lis[i]) + " " + add_ons[i] + res
            if i != len(lis) - 1:
                res = " " + res
            
        return res.rstrip()