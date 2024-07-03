class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE & divisor == -1){
            return Integer.MAX_VALUE;
        }
        
        int sign = (dividend > 0) == (divisor > 0) ? 1 : -1;
        
        long div = Math.abs((long) dividend);
        long ds = Math.abs((long) divisor);
        
        int res = 0;
        
        while (div >= ds){
            long temp = ds;
            int mul = 1;
            
            while (div >= (temp << 1)){
                temp <<= 1;
                mul <<= 1;
            }
            
            div -= temp;
            res += mul;
        }
        
        return sign * res;
    }
}