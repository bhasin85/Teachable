# 1->2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #self._print(head)
        return self.reverse(head)
        
    def reverse(self, curr, prev=None):
        if not curr:
            return prev # tail node
        temp = curr.next
        curr.next = prev
        return self.reverse(temp, curr)
            
    def _print(self, node):
        output = ""
        while node:
            output += "->{}".format(node.val)
            node = node.next
            
        print(output)
