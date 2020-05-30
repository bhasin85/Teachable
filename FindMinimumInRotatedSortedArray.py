# [4,5,6,7,0,1,2] 
# left   : 7
# right  : 0
# center : 7
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return min(nums[0], nums[1])
        
        length = len(nums)
        left, center, right = 0, length//2, length - 1
        _min = min(nums[left], nums[center], nums[right])
        
        while right > left:                
            if nums[center] > nums[center+1]:
                return nums[center+1]

            if nums[center-1] > nums[center]:
                return nums[center]
            
            if nums[center] > nums[right]:
                left = center
            else:
                right = center
            center = (left+right)//2
