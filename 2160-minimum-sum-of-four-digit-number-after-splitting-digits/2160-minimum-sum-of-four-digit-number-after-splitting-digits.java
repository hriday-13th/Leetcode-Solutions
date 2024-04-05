class Solution {
    public int minimumSum(int num) {
        String str = Integer.toString(num);
        int[] arr = new int[str.length()];
        
        for (int i=0; i<str.length(); i++){
            arr[i] = Character.getNumericValue(str.charAt(i));
        }
        
        Arrays.sort(arr);
        
        int f = arr[0]*10 + arr[str.length()-1];
        int s = arr[1]*10 + arr[str.length()-2];
        
        return f+s;
    }
}