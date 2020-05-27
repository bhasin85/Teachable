class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.searchRangeRec(nums, target, 0)
        
    def searchRangeRec(self, nums: List[int], target: int, adjustment: int) -> List[int]:
        #print("Input:{} target:{}".format(nums, target))
        length = len(nums)
        
        if length == 1 and nums[0] == target:
            return [0+adjustment, 0+adjustment]
        
        if length == 0 or length == 1:
            return [-1, -1]

        mid = length//2
        print("Input:{} target:{} mid:{} adjustment:{} Left:{} Right:{}".format(nums, target, nums[mid], adjustment, nums[:mid], nums[mid:]))
        if nums[mid] == target:
            left, right = mid, mid
            # find leftmost
            while left-1>=0 and nums[left-1]==target:
                left -= 1
            
            # find rightmost
            while right+1<len(nums) and nums[right+1]==target:
                right += 1
            
            return [left+adjustment, right+adjustment]
        elif nums[mid] > target:
            # find in left subarray
            return self.searchRangeRec(nums[:mid], target, adjustment)
        elif nums[mid] < target:
            # find in right subarray
            return self.searchRangeRec(nums[mid:], target, adjustment+len(nums[:mid]))
