class Solution {
    public String restoreString(String s, int[] indices) {
        char[] arr = new char[s.length()];
        
        for (int i=0; i<s.length(); i++){
            int ind = indices[i];
            char ch = s.charAt(i);
            
            arr[ind] = ch;
        }
        String st = new String(arr);
        return st;
    }
}