class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        _max = nums[0]
        start = 0
        for current in range(1, len(nums)):
            start_sum = sum(nums[start:current+1])
            current_sum = nums[current]
            
            if current_sum > start_sum:
                start = current
                _max = max(_max, current_sum)
            else:
                _max = max(_max, start_sum)
        
        return _max
