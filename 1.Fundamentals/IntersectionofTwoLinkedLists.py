# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        intersection_node = None
        pointerA = headA
        pointerB = headB
        
        if pointerA is None or pointerB is None:
            return intersection_node
            
        while pointerA or pointerB:
            if pointerA == pointerB:
                intersection_node = pointerA
                break
            
            if pointerA is None:
                pointerA = headB
            else:
                pointerA = pointerA.next
                
            if pointerB is None:
                pointerB = headA
            else:
                pointerB = pointerB.next
                
        return intersection_node

# First solution
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         intersection_node = None
#         skipA = headA
        
#         while skipA:
#             skipB = headB
#             while skipB:
#                 if skipA.val == skipB.val and skipA == skipB:
#                     intersection_node = skipA
#                     return intersection_node 
#                 skipB = skipB.next
#             skipA = skipA.next
            
#         return intersection_node
        
