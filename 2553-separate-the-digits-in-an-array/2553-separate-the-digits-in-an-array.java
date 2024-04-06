class Solution {
    public int[] separateDigits(int[] nums) {
        ArrayList<Integer> arr = new ArrayList();
        
        for (int i : nums){
            String s = i + "";
            
            for (int j=0; j<s.length(); j++){
                arr.add(Integer.parseInt(s.charAt(j) + ""));
            }
        }
        
        int[] res = new int[arr.size()];
        for (int i=0; i<res.length; i++){
            res[i] = arr.get(i);
        }
        
        return res;
    }
}