class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int cnt = 0;
        int val = tickets[k];
        
        for (int i=0; i<tickets.length; i++){
            if (i <= k){
                cnt += Math.min(val, tickets[i]);
            }
            else{
                cnt += Math.min(val-1, tickets[i]);
            }
        }
        return cnt;
    }
}