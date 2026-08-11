# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        ptr = self
        print("[", end="")
        while ptr:
            print(ptr.val, end=',')
            ptr = ptr.next
        print("]")

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None #head of result LinkedList
        l_ptr = None #used to build new List
        tmp = None #the item being inserted each iteration
        A, B = list1, list2
        
        while A or B:
            if not B: #B is empty, default to A
                tmp = A
                A = A.next
            elif not A: #A is empty, default to B
                tmp = B
                B = B.next
            elif A.val < B.val: #Both have contents, A smaller
                tmp = A
                A = A.next
            elif B.val <= A.val: #Both have contents, B smaller
                tmp = B
                B = B.next
            # Build list
            if not head: #first element
                head = l_ptr = tmp
            else:
                l_ptr.next = tmp
                l_ptr = l_ptr.next

        return head

L1 = ListNode(1, ListNode(2, ListNode(4, None)))
L2 = ListNode(1, ListNode(3, ListNode(4, None)))
        