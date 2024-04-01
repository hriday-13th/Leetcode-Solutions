class Solution {
    public boolean isPrefixString(String s, String[] words) {
        for (String word : words){
            if (s == ""){
                return true;
            }
            if (!s.startsWith(word)){
                return false;
            }
            s = s.substring(word.length());
        }
        return s.equals("");
    }
}