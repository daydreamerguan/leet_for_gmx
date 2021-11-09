# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        exist_set = set()
        ret_head = None
        cnt_node = head
        cnt_new_node = None
        while cnt_node:
            if cnt_node.val not in exist_set:
                exist_set.add(cnt_node.val)
                if not ret_head:
                    ret_head = ListNode(cnt_node.val, None)
                    cnt_new_node = ret_head
                else:
                    new_node = ListNode(cnt_node.val, None)
                    cnt_new_node.next = new_node
                    cnt_new_node = new_node
            cnt_node = cnt_node.next
        return ret_head
