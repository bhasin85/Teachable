# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

 
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        stack = list()
        curr = head
        centre_found = False
        
        while curr: 
            # Start comparing with the previous elements stored in stack
            if centre_found:
                if len(stack) == 0:
                    return False
                
                pop = stack.pop()
                if pop != curr.val:
                    return False
                
                curr = curr.next
            else:
                # Odd -> 1,2,3,2,1
                if curr.next and curr.next.next and curr.val == curr.next.next.val:
                    stack.append(curr.val)
                    curr = curr.next.next
                    centre_found = True
                # Even -> 1,2,2,1
                elif curr.next and curr.val == curr.next.val:
                    stack.append(curr.val)
                    curr = curr.next
                    centre_found = True
                else:
                    stack.append(curr.val)
                    curr = curr.next
          
        if not curr and len(stack) == 0 and centre_found:
            return True
            
        return False
            
            
