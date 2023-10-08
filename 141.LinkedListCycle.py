# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        faster_pointer = self.move_fast(head)
        slow_pointer = self.move_slow(head)
        while faster_pointer and slow_pointer:
            if faster_pointer is slow_pointer:
                return True
            faster_pointer = self.move_fast(faster_pointer)
            slow_pointer = self.move_slow(slow_pointer)
        return False

    def move_fast(self, head):
        return self.move_slow(self.move_slow(head))

    def move_slow(self, head):
        if not head:
            return None
        return head.next