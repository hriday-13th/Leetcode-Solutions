class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int[] row : matrix){
            if (row[0] <= target && target <= row[row.length-1]){
                if (search(row, target)) return true;
            }
        }
        return false;
    }
    
    public boolean search(int[] arr, int k){
        int l = 0;
        int h = arr.length - 1;
        
        while (l <= h){
            int m = (l+h) / 2;
            
            if (arr[m] == k) return true;
            else if (arr[m] > k){
                h = m - 1;
            }
            else {
                l = m + 1;
            }
        }
        return false;
    }
}