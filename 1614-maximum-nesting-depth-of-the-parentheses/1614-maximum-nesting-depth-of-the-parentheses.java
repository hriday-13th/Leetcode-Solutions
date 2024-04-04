class Solution {
    public int maxDepth(String s) {
        char[] chars = s.toCharArray();
        int m = 0;
        int count = 0;
        
        for (int i=chars.length-1; i > -1; i--){
            if (chars[i] == ')'){
                count++;
                m = Math.max(m, count);
            }
            else if (chars[i] == '('){
                count--;
                m = Math.max(m, count);
            }
        }
        return m;
    }
}