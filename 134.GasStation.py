class Node(object):
    def __init__(self, val, index, next_node=None):
        self.val = val
        self.index = index
        self.next_node = next_node

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        size = len(gas)
        diff_list = []
        for i in xrange(0, size):
            diff_list.append(Node(gas[i] - cost[i], i))

        for i in xrange(0, size):
            diff_list[i].next_node = diff_list[(i + 1) % size]

        cnt_node = diff_list[0]
        max_loop_size = size + 1
        cnt_loop = 0
        while cnt_node.next_node != cnt_node:
            if cnt_loop > max_loop_size:
                return -1
            if cnt_node.val > 0:
                cnt_loop = 0
                max_loop_size -= 1
                self.mergeNode(cnt_node)
            else:
                cnt_loop += 1
                cnt_node = cnt_node.next_node
        return cnt_node.index if cnt_node.val >= 0 else -1

    def mergeNode(self, node):
        node.val += node.next_node.val
        node.next_node = node.next_node.next_node
