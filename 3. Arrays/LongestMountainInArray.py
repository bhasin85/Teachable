#           
#    a       b
# [2,1,4,7,3,2,5]
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        longest = 0
        i = 1
        
        if len(A) < 3:
            return longest
        
        while i <= len(A)-2:
            # Check for height
            height = 1
            while i-height>=0 and i+height<len(A):
                left = i - height
                right = i + height

                if A[left] < A[left+1] and A[right] < A[right-1]:
                    longest = max(longest, height)
                    height += 1
                    #print("true")
                else:
                    #print("false")
                    break
            
            i += 1
        
        if longest>0:
            return longest * 2 + 1
        else:
            return longest
