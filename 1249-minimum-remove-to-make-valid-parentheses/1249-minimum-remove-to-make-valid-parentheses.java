class Solution {
    public String minRemoveToMakeValid(String s) {
        ArrayList<Character> arr = new ArrayList<>();
        char[] l = s.toCharArray();
        int count = 0;

        for (char ch : l) {
            if (ch == '(') {
                arr.add(ch);
                count++;
            } else if (ch == ')' && count > 0) {
                arr.add(ch);
                count--;
            } else if (ch != ')') {
                arr.add(ch);
            }
        }

        ArrayList<Character> res = new ArrayList<>();

        for (int i = arr.size()-1; i>-1 ; i--) {
            if (arr.get(i) == '(' && count > 0) {
                count--;
            } else {
                res.add(arr.get(i));
            }
        }

        StringBuilder ans = new StringBuilder();
        for (Character c : res) {
            ans.append(c);
        }

        return ans.reverse().toString();
    }
}