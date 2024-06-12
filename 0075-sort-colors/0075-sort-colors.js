/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    var ind = 0;
    
    for (let i=0; i<nums.length; i++){
        if (nums[i] == 0){
            let t = nums[ind];
            nums[ind] = 0;
            nums[i] = t;
            ind++;
        }
    }
    
    for (let j=ind; j<nums.length; j++){
        if (nums[j] == 1){
            let t = nums[ind];
            nums[ind] = 1;
            nums[j] = t;
            ind++;
        }
    }
};