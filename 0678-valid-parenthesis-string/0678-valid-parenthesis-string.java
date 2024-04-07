class Solution {
    public boolean checkValidString(String s) {
        int l = 0;
        int h = 0;
        
        for (char i : s.toCharArray()){
            if (i == '('){
                l++; h++;
            }
            else if (i == ')'){
                l--; h--;
            }
            else {
                l--; h++;
            }
            if (h < 0){
                return false;
            }
            if (l < 0){
                l = 0;
            }
        }
        return l == 0;
    }
}