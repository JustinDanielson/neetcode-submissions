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
    # 2 Pointer Solution
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        follower = leader = head
        for _ in range(n):
            leader = leader.next
        # n will always be within 1 to length of list
        if not leader:
            return head.next
        
        # advance follower and leader until leader reaches the end
        while leader.next:
            follower = follower.next
            leader = leader.next
        follower.next = follower.next.next
        
        return head

#    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#        stack = []
#        ptr = head
#        # Put all elements on stack
#        while ptr:
#            stack.append(ptr)
#            ptr = ptr.next
#        
#        # Pop nodes to get to nth element
#        while n and stack:
#            stack.pop()
#            n -= 1 #don't forget this, lol
#        
#        # If there are elements left on stack, we are removing a body node
#        if len(stack) > 0:
#            node = stack.pop()
#            if node and node.next:
#                node.next = node.next.next
#            else: # removing last element
#                node.next = None
#        # No elements left, so remove the head node
#        else:
#            head = head.next
#
#        return head
        
