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
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode[] arr = new ListNode[k];
        
        int l = 0;
        ListNode curr_t = head;
        
        while (curr_t != null){
            curr_t = curr_t.next;
            l++;
        }
        
        int d = l / k;
        int rem = l % k;
        
        ListNode curr = head;
        
        for (int i=0; i < k; i++){
            int size = d + (i < rem ? 1 : 0);
            arr[i] = curr;
            
            for (int j=0; j<size - 1; j++){
                if (curr != null) curr = curr.next;
            }
            
            if (curr != null){
                ListNode temp = curr.next;
                curr.next = null;
                curr = temp;
            }
        }
        
        return arr;
    }
}