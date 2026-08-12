# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        res = ""
        h = self
        while h:
            res += str(h.val)
            h = h.next
            if h:
                res += "->"
        return res

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        ptr = head
        # Put all elements on stack
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        
        # Pop nodes to get to nth element
        while n and stack:
            stack.pop()
            n -= 1 #don't forget this, lol
        
        # If there are elements left on stack, we are removing a body node
        if len(stack) > 0:
            node = stack.pop()
            if node and node.next:
                node.next = node.next.next
            else: # removing last element
                node.next = None
        # No elements left, so remove the head node
        else:
            head = head.next

        return head
        
