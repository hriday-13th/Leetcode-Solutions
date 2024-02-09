public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        int checker;
        
        for (int i=0; i<32; i++){
            checker = (n & 1);
            if (checker == 1) count += 1;
            n >>>= 1;
        }
        return count;
    }
}