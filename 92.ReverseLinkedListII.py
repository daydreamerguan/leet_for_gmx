
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left >= right:
            return head
        cnt_index = 1
        cnt_node = head
        node_stack = []
        pre_node = None
        while cnt_node != None:
            if cnt_index == left - 1:
                pre_node = cnt_node
            if cnt_index >= left and cnt_index <= right:
                    node_stack.append(cnt_node)
            cnt_node = cnt_node.next
            cnt_index += 1
            if cnt_index == right + 1 or cnt_node == None:
                while node_stack:
                    node = node_stack.pop()
                    if not node_stack:
                        node.next = cnt_node
                    if not pre_node:
                        pre_node = node
                        head = node
                        continue
                    pre_node.next = node
                    pre_node = node
                break
        return head


def print_list(node):
    while node:
        print node.val
        node = node.next

def makeList(input_list):
    ret_list = [ListNode(i) for i in input_list]
    for i, node in enumerate(ret_list):
        if i != 0:
            ret_list[i - 1].next = node
    return ret_list[0]


if __name__ == '__main__':
    print_list(Solution().reverseBetween(makeList([1,2,3,4,5]), 2, 4))
