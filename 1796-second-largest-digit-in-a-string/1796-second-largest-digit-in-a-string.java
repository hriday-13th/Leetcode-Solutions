class Solution {
    public int secondHighest(String s) {
        int max = -1;
        int sec_max = -1;
        
        for (char c : s.toCharArray()){
            if (Character.isDigit(c)){
                int val = Character.getNumericValue(c);
                if (val > max){
                    sec_max = max;
                    max = val;
                }
                else if (val < max && val > sec_max){
                    sec_max = val;
                }
            }
        }
        return sec_max;
    }
}