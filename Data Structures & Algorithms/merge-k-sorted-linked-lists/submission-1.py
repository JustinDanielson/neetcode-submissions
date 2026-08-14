# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# You are given an array of `k` linked lists, where each list is sorted in ascending order
class Solution:    
    def _min_indicies(self, lists):
        res = []
        min_found = float("inf")
        for i in range(0, len(lists)):
            if lists[i] and lists[i].val < min_found:
                res.clear()
                res.append(i)
                min_found = lists[i].val
            elif lists[i] and lists[i].val == min_found:
                res.append(i)
        return res
    
    def _pop_all(self, lists, indicies, target):
        '''
        Given an array of indicies, pop the top n elements containing the same value
        '''
        ptr = result = ListNode()
        tail = None
        for index in indicies:
            item = lists[index]
            # if item @ lists[index] has .next nodes with same values, then pop
            # the whole chain of dupes and keep track of tail node
            while lists[index] and lists[index].val == target:
                tail = lists[index]
                lists[index] = lists[index].next
            ptr.next = item
            ptr = tail
        return result.next, ptr
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ptr = result = ListNode()
        indicies = self._min_indicies(lists)
        while indicies:
            ptr.next, tail_node = self._pop_all(lists, indicies, lists[indicies[-1]].val)
            ptr = tail_node
            indicies = self._min_indicies(lists)

        return result.next