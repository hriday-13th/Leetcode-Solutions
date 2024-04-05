class Solution {
    public int differenceOfSum(int[] nums) {
        int ele = 0;
        int dig = 0;
        
        for (int i : nums){
            ele += i;
            
            int temp = i;
            while (temp > 0){
                dig += (temp % 10);
                temp /= 10;
            }
        }
        return Math.abs(ele - dig);
    }
}