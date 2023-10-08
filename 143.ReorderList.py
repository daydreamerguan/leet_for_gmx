# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        node_list = []
        cnt_node = head
        while cnt_node:
            node_list.append(cnt_node)
            cnt_node = cnt_node.next

        left_index = 0
        right_index = len(node_list) - 1
        cnt_node = head
        mode = 0 # 0 link right most 1 link left most
        while left_index < right_index and cnt_node:
            next_node = None
            if mode == 0:
                next_node = node_list[right_index]
                left_index += 1
            else:
                next_node = node_list[left_index]
                right_index -= 1
            mode = (mode + 1) % 2
            cnt_node.next = next_node
            cnt_node = next_node
        cnt_node.next = None # last one