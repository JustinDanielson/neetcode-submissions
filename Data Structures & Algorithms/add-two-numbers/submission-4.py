# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # This solution could integer overflow num1 and num2
    # Bc the lists of numbers are in reverse order (ex: 321 is [1]->[2]->[3])
    # A solution can add digits from l1 and l2 and then use %10 and //10 to
    # calculate the carry value and the digit.
    # Using this approach, the 2 loops can be combined for a single pass solution
    # TODO: Implement this better solution if you want to practice Linked Lists
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_ptr = res = ListNode()
        num1 = num2 = count = 0
        a_has_digits = a = l1
        b_has_digits = b = l2
        while a or b:
            if a_has_digits:
                num1 += a.val * 10**count
                a_has_digits = a = a.next
            if b_has_digits:
                num2 += b.val * 10**count
                b_has_digits = b = b.next
            count += 1
        num3 = num1 + num2

        while num3 >= 10:
            res_ptr.val = num3 % 10
            res_ptr.next = ListNode()
            num3 //= 10
            res_ptr = res_ptr.next
        res_ptr.val = num3 # handle last digit

        return res
