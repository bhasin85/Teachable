class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k <= 0:
            return 0
        
        result = 0
        product = 1
        left, right = 0, 0

        while right < len(nums):
            #print("left:{} right:{} {}".format(left, right, nums[left:right+1]))
            product *= nums[right]
            
            while product >= k and left < right:
                product = product // nums[left]
                left += 1
                
            if product < k:
                result += right - left + 1
            right += 1
            
        return result
        
