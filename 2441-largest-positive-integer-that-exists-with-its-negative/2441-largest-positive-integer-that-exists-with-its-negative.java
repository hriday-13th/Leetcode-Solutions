class Solution {
    public int findMaxK(int[] nums) {
        Arrays.sort(nums);
        int i = 0;
        int j = nums.length - 1;
        
        while (i < j){
            if (nums[i] < 0) {
                int val = Math.abs(nums[i]);
                if (nums[j] == val) return nums[j];
                else if (nums[j] > val) j--;
                else if (nums[j] < val) i++;
            }
            else{
                return -1;
            }
        }
        return -1;
    }
}