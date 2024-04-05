class Solution {
    public int minLength(String s) {
        ArrayList<Character> arr = new ArrayList();
        
        for (int i=0; i<s.length(); i++){
            if (arr.isEmpty()){
                arr.add(s.charAt(i));
            }
            else {
                char top = arr.get(arr.size() - 1);
                char curr = s.charAt(i);
                
                if ((Character.toUpperCase(top) == 'A' && Character.toUpperCase(curr) == 'B') ||
                    (Character.toUpperCase(top) == 'C' && Character.toUpperCase(curr) == 'D')){
                    arr.remove(arr.size() - 1);
                }
                else {
                    arr.add(s.charAt(i));
                }
            }
        }
        return arr.size();
    }
}