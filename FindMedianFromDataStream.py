#[1, 2][3, 4]
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_max = []
        self.right_min = []
        

    def addNum(self, num: int) -> None:
        left_length, right_length = len(self.left_max), len(self.right_min)
        left = self.left_max[0] * -1 if left_length > 0 else float('-inf')
        right = self.right_min[0] if right_length > 0 else float('-inf')
        
        # num < left
            # check lenght of heaps
                # equal lengths -> go to left
                
                # left length > right
                    # pop left -> insert it to right -> add new num to left 
        if left_length == 0:
            heapq.heappush(self.left_max, num * -1)              
        elif num < left:
            if left_length == right_length:
                heapq.heappush(self.left_max, num * -1)
            elif left_length > right_length:
                pop = heapq.heappop(self.left_max) * -1
                heapq.heappush(self.right_min, pop)
                heapq.heappush(self.left_max, num * -1)
        elif left <= num <= right:
            if left_length == right_length:
                heapq.heappush(self.left_max, num * -1)
            elif left_length > right_length:
                heapq.heappush(self.right_min, num)     
        elif num > right:
            if left_length == right_length:
                pop = heapq.heappop(self.right_min)
                heapq.heappush(self.left_max, pop * -1)
                heapq.heappush(self.right_min, num)
            elif left_length > right_length:
                heapq.heappush(self.right_min, num)       
                
        # print("addNum: num:{} left_max:{} {}:{} right_min:{}".format(num, self.left_max, left, right, self.right_min))
        # left < num < right
                # equal lengths -> go to left
                
                # left length > right
                    # insert it to right
        # num > right
                # equal lengths -> go to left
                    # pop from right -> insert pop to left -> insert num to right
                
                # left length > right
                    # insert it to right
                
    def findMedian(self) -> float:
        left_length, right_length = len(self.left_max), len(self.right_min)
        left = self.left_max[0] * -1 if left_length > 0 else float('-inf')
        right = self.right_min[0] if right_length > 0 else float('-inf')
        
        median = (left + right) / 2 if left_length == right_length else left
        # print("Median:{} left_max:{} {}:{} right_min:{}".format(median, self.left_max, left, right, self.right_min))
        
        return median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
