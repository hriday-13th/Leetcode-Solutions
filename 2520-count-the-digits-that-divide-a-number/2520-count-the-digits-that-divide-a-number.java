class Solution {
    public int countDigits(int num) {
        ArrayList<Integer> ls = new ArrayList<>();
        
        int tmp = num;
        while (tmp > 0){
            int val = tmp % 10;
            ls.add(val);
            tmp /= 10;
        }
        
        int count = 0;
        for (int i : ls){
            if (num % i == 0) count++;
        }
        
        return count;
    }
}