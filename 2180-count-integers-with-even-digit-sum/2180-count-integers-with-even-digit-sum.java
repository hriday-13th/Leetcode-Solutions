class Solution {
    public int countEven(int num) {
        int res = 0;
        
        for (int i=1; i <= num; i++){
            int val = digiSum(i);
            if (val % 2 == 0) res++;
        }
        return res;
    }
    
    private int digiSum(int i){
        int temp = 0;
        while (i > 0){
            temp += i % 10;
            i /= 10;
        }
        return temp;
    }
}