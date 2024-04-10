class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;
        
        do {
            slow = cal(slow);
            fast = cal(cal(fast));
        } while (slow != fast);
        
        return slow == 1;
    }
    
    public int cal(int i){
        int ans = 0;
        
        while (i > 0){
            int temp = i % 10;
            ans += temp * temp;
            i /= 10;
        }
        
        return ans;
    }
}