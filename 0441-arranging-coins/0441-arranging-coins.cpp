class Solution {
public:
    int arrangeCoins(int n) {
        int res = 0, req = 1;
        
        while(req <= n){
            res++;
            n -= req;
            req++;
        }
        return res;
    }
};