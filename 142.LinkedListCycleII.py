# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cnt_node = head
        visited_set = set()
        while cnt_node:
            if cnt_node in visited_set:
                return cnt_node
            visited_set.add(cnt_node)
            cnt_node = cnt_node.next
        return None
