# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Shuffle the list so that the back half is reversed and shuffled into the 
        # first half. Alternating in ABABABAB order where B is the reversed half.
        stack = []
        l_ptr = head
        while l_ptr:
            stack.append(l_ptr)
            l_ptr = l_ptr.next
        
        # shuffle
        num_elements = len(stack)
        l_ptr = head
        for _ in range(num_elements // 2):
            temp = l_ptr.next
            # insert stack between head & temp(head.next)
            top = stack.pop()
            top.next = temp
            l_ptr.next = top
            # set l_ptr to l_ptr.next.next
            l_ptr = temp
        
        l_ptr.next = None
        # if odd num of elements, grab 1 more from stack
        if num_elements & 1:
            l_ptr.next = stack.pop()
            l_ptr.next.next = None