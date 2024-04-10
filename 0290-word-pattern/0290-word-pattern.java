class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] ls = s.split(" ", -1);
        
        if (pattern.length() != ls.length) return false;
        
        HashMap<Character, String> map = new HashMap<>();
        
        for (int i=0; i<pattern.length(); i++){
            char curr = pattern.charAt(i);
            if (!map.containsKey(curr)){
                if (!map.containsValue(ls[i])){
                    map.put(curr, ls[i]);
                }
                else{
                    return false;
                }
            }
            else if (!map.get(curr).equals(ls[i])) return false;
        }
        return true;
    }
}