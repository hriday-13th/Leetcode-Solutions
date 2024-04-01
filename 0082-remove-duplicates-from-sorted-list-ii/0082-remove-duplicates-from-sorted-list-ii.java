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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        
        HashMap<Integer, Integer> map = new HashMap<>();
        ListNode curr = head;
        
        while (curr != null){
            int val = curr.val;
            map.put(val, map.getOrDefault(val, 0) + 1);
            curr = curr.next;
        }
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        curr = head;
        
        while (curr != null){
            int val = curr.val;
            if (map.containsKey(val) && map.get(val) > 1) {
                prev.next = curr.next;
            } else {
                prev = curr;
            }
            curr = curr.next;
        }
        return dummy.next;
    }
}