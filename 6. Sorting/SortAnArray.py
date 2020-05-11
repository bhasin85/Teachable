class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        
        pivot = len(nums)//2
        left = nums[0:pivot]
        right = nums[pivot:len(nums)]
        
        return self.merge(self.sortArray(left), self.sortArray(right))
    
    
    def merge(self, left, right):
        leftIndex = 0
        rightIndex = 0
        left_size = len(left)
        right_size = len(right)
        result = []
        
        while leftIndex < left_size or rightIndex < right_size:
            
            if leftIndex < left_size and rightIndex < right_size:
                # both arrays have elements
                if left[leftIndex]<right[rightIndex]:
                    result.append(left[leftIndex])
                    leftIndex += 1
                else:
                    result.append(right[rightIndex])
                    rightIndex += 1
            elif leftIndex < left_size and rightIndex == right_size:
                # left array have elements
                result.append(left[leftIndex])
                leftIndex += 1                
            elif leftIndex == left_size and rightIndex < right_size:
                # right array have elements
                result.append(right[rightIndex])
                rightIndex += 1 
                
        return result
