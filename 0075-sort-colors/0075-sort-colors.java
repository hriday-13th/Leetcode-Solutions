class Solution {
    public void sortColors(int[] nums) {
        int ind = 0;
        
        for (int i=0; i<nums.length; i++){
            if (nums[i] == 0){
                int t = nums[ind];
                nums[ind] = 0;
                nums[i] = t;
                ind++;
            }
        }
        
        for (int j=ind; j<nums.length; j++){
            if (nums[j] == 1){
                int t = nums[ind];
                nums[ind] = 1;
                nums[j] = t;
                ind++;
            }
        }
    }
}