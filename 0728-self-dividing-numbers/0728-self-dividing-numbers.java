class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        ArrayList<Integer> res = new ArrayList<>();
        
        for (int num=left; num<right+1; num++){
            int temp = num;
            boolean flag = true;
            while (temp > 0){
                int div = temp % 10;
                if (div == 0 || num % div != 0){
                    flag = false;
                    break;
                }
                temp /= 10;
            }
            if (flag) res.add(num);
        }
        return res;
    }
}