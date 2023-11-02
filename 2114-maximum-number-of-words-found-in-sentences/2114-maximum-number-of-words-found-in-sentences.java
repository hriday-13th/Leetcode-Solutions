class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 0;
        for (String s : sentences){
            char[] ar = s.toCharArray();
            int count = 0;
            for (char c : ar){
                if (c == ' '){
                    count++;
                }

                if (count + 1 > max){
                    max = count + 1;
                }
            }

        }
        return max;
    }
}