class Solution {
    public int maxSubArray(int[] nums) {
        int high = Integer.MIN_VALUE;
        int till = 0;
        
        for (int i : nums){
            till += i;
            
            if (high < till){
                high = till;
            }
            
            if (till < 0){
                till = 0;
            }
        }
        return high;
    }
}