class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        int count, pop;
        for (int i=0; i<n+1; i++){
            count = 0;
            int num = i;
            while (num != 0){
                count += (num & 1);
                num >>>= 1;
            }
            res[i] = count;
        }
        return res;
    }
}