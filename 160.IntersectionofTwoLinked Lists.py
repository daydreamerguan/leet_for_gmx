# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited_heads = set()
        cnt_a = headA
        while cnt_a:
            visited_heads.add(cnt_a)
            cnt_a = cnt_a.next

        cnt_b = headB
        while cnt_b:
            if cnt_b in visited_heads:
                return cnt_b
            cnt_b = cnt_b.next
        return None