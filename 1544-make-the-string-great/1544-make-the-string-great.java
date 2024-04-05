class Solution {
    public String makeGood(String s) {
        if (s.length() == 1){
            return s;
        }
        
        ArrayList<Character> stack = new ArrayList<Character>();
        
        for (int i=0; i<s.length(); i++){
            if (stack.isEmpty()){
                stack.add(s.charAt(i));
            }
            else {
                char top = stack.get(stack.size()-1);
                char curr = s.charAt(i);

                if (Character.toLowerCase(top) == Character.toLowerCase(curr) && top != curr){
                    stack.remove(stack.size()-1);
                }
                else{
                    stack.add(curr);
                }
            }
        }
        StringBuilder res = new StringBuilder();
        for (char ch : stack){
            res.append(ch);
        }
        
        return res.toString();
    }
}