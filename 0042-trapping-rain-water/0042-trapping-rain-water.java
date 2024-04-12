class Solution {
    public int trap(int[] height) {
        int n = height.length;
        
        if (n == 1) return 0;
        
        int[] left = new int[n];
        int[] right = new int[n];
        
        left[0] = height[0];
        for (int i=1; i<n; i++){
            left[i] = Math.max(height[i], left[i-1]);
        }
        
        right[n-1] = height[n-1];
        for (int j=n-2; j>-1; j--){
            right[j] = Math.max(height[j], right[j+1]);
        }
        
        int net = 0;
        for (int x=0; x<n; x++){
            net += Math.min(left[x], right[x]) - height[x];
        }
        return net;
    }
}