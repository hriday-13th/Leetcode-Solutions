class Solution {
    public int lengthOfLastWord(String s) {
        int count = 0;
        for (int i=s.length()-1; i >= 0; i--){
            char ele = s.charAt(i);
            if (Character.isLetter(ele)){
                count++;
            }
            else if (ele == ' ' && count != 0){
                break;
            }
        }
        return count;
    }
}