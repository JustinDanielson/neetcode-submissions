"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newlist = None
        old_to_new = dict()
        length = 0

        if not head:
            return None

        ptr = head
        newlist_ptr = newhead = Node(0)
        while ptr:
            new_node = Node(ptr.val, None, None) #create deep copy
            newlist_ptr.next = new_node #insert it into list
            old_to_new[hash(ptr)] = new_node #map old node to its deepcopy
            # advance both lists
            ptr = ptr.next
            newlist_ptr = newlist_ptr.next
        
        ptr = head
        newlist_ptr = newhead.next #.next bc newhead is dummy node
        while ptr:
            # handle random map
            if ptr.random:
                newlist_ptr.random = old_to_new[hash(ptr.random)]
            # advance both lists
            newlist_ptr = newlist_ptr.next
            ptr = ptr.next

        return newhead.next #skip dummy node

