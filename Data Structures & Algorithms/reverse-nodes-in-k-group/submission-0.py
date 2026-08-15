# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        res = str(self.val)
        ptr = self.next
        while ptr:
            res += "->" + str(ptr.val)
            ptr = ptr.next
        return res

class Solution:
    # Reverses a singly linked list between start end end
    # and returns the new start and end pointer pairs
    def reverseK(self, start, end):
        cur = start
        tmp = prev = None
        while prev != end:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        start.next = tmp
        return end, start
 
 
    # You are given the head of a singly linked list and k
    # Reverse every segment of k length elements.
    # If there are fewer than k nodes, don't reverse them
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = None
        start = end = head
        previous_end = None
        while end:
            l = r = end
            # Look ahead to see if there is a segment of length k
            for _ in range(k-1):
                r = r.next if r else None

            # If there is a valid k length segment
            if r:
                # Reverse that segment
                start, end = self.reverseK(l, r)
                # the previous segment's end pointed to `l` bc it was unknown if
                # a next segement existed. update it to point to r. (r == start is True)
                if previous_end and r == start:
                    previous_end.next = r
                previous_end = end
                # advance end to see if more elements exist
                end = end.next
                # the new head is the right pointer of the first segment that was reversed
                if not new_head:
                    new_head = r
            else:
                end = None
        return new_head if new_head else start


#lst = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
#start = lst
#Solution().reverseKGroup(lst, 3)