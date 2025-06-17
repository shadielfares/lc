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
    public ListNode insertionSortList(ListNode head) {
      ListNode current = head;
      List<Integer> arrayList = new ArrayList<>();
      while (current != null){
            arrayList.add(current.val);
            current = current.next;
        }
        Collections.sort(arrayList);
        current = head;
        for (int val : arrayList){
            current.val = val;
            current = current.next;
        }
        return head;
    }
}   