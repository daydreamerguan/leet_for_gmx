# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        size = self.count_size(head)
        half_size = size / 2
        right_head = self.get_kth_node(half_size, head)
        right_head = self.reverseList(right_head)

        while head and right_head:
            if head.val != right_head.val:
                return False
            head = head.next
            right_head = right_head.next
        return True

    def reverseList(self, head):
        parent = None
        cnt_node = head
        if cnt_node is None:
            return None
        while cnt_node.next != None:
            next_node = cnt_node.next
            cnt_node.next = parent
            parent = cnt_node
            cnt_node = next_node
        cnt_node.next = parent
        return cnt_node

    def get_kth_node(self, k, node):
        index = 0
        while index < k:
            node = node.next
            index += 1
        return node
    
    def count_size(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size