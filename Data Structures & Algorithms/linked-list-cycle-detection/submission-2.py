# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_iter = slow_iter = head
        while slow_iter and slow_iter.next:
            for i in range(3):
                fast_iter = fast_iter.next
                if fast_iter == None:
                    return False
                if hash(fast_iter) == hash(slow_iter):
                    return True
            slow_iter = slow_iter.next
        return False