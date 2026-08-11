# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev_node = None
        cur_node = head
        tmp_node = None
        while cur_node:
            tmp_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = tmp_node
        
        return prev_node