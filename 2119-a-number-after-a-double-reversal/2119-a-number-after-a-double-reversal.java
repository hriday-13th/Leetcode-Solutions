class Solution {
    public boolean isSameAfterReversals(int num) {
        int rev1 = 0;
        int rev2 = 0;
        int pop;
        int temp = num;
        
        while (num != 0){
            pop = num % 10;
            num /= 10;
            
            rev1 = (rev1 * 10) + pop;
        }
        
        while (rev1 != 0){
            pop = rev1 % 10;
            rev1 /= 10;
            
            rev2 = (rev2 * 10) + pop;
        }
        
        if (rev2 == temp) return true;
        else return false;
    }
}