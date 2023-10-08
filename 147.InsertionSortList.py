# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        linked_list = []
        cnt_node = head
        while cnt_node:
            linked_list.append(cnt_node)
            cnt_node = cnt_node.next
        list_size = len(linked_list)
        for i in xrange(1, list_size):
            cnt_index = i
            while cnt_index > 0 and linked_list[cnt_index].val < linked_list[cnt_index  - 1].val:
                temp = linked_list[cnt_index]
                linked_list[cnt_index] = linked_list[cnt_index  - 1]
                linked_list[cnt_index  - 1] = temp
                cnt_index -= 1
        
        for i in xrange(0, list_size):
            if i < list_size - 1 :
                linked_list[i].next = linked_list[i + 1]
            else:
                linked_list[i].next = None
        return linked_list[0]
