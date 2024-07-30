class Solution {
    public int minimumDeletions(String s) {
        char[] arr = s.toCharArray();
        int count_b = 0;
        int min_del = 0;
        
        for (int i=0; i<arr.length; i++){
            if (arr[i] == 'a'){
                min_del = Math.min(min_del + 1, count_b);
            }
            else{
                count_b++;
            }
        }
        
        return min_del;
    }
}