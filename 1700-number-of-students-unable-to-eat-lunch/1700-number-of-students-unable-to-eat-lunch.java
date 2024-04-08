class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int[] count = new int[2];
        
        for (int i : students) count[i]++;
        
        int rem = sandwiches.length;
        
        for (int i : sandwiches){
            if (count[i] == 0) break;
            if (rem-- == 0) break;
            count[i]--;
        }
        return rem;
    }
}