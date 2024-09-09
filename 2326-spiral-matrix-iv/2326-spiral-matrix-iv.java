/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] arr = new int[m][n];
        
        for (int i=0; i < m; i++){
            for (int j=0; j < n; j++){
                arr[i][j] = -1;
            }
        }
        
        ListNode curr = head;
        int cs = 0;
        int ce = n - 1;
        int rs = 0;
        int re = m - 1;
        
        while (curr != null){
            for (int i=cs; i <= ce && curr != null; i++){
                arr[rs][i] = curr.val;
                curr = curr.next;
            }rs++;
            
            for (int i=rs; i <= re && curr != null; i++){
                arr[i][ce] = curr.val;
                curr = curr.next;
            }ce--;
            
            for (int i=ce; i >= cs && curr != null; i--){
                arr[re][i] = curr.val;
                curr = curr.next;
            }re--;
            
            for (int i=re; i >= rs && curr != null; i--){
                arr[i][cs] = curr.val;
                curr = curr.next;
            }cs++;
        }
        
        return arr;
    }
}