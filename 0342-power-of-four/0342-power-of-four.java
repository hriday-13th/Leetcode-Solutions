class Solution {
    public boolean isPowerOfFour(int n) {
        int i = 0;
        /*if (Math.pow(4,i) < n){
            i++;
        }
        else if (Math.pow(4,i) == n){
            return true;
        }
        return false;*/


        while (Math.pow(4,i) < n){
            i++;
        }

        if (Math.pow(4,i) == n){
            return true;
        }
        else{
            return false;
        }
    }
}