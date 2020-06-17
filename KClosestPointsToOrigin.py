import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        data = [(self.get_distance(point), point) for point in points]
        heapq.heapify(data)
        #print(data)
        return [entry[1] for entry in heapq.nsmallest(K, data)]
        
    def get_distance(self, point):
        plot1 = [0, 0]
        plot2 = point
        euclidean_distance = sqrt( (plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2 )
        return euclidean_distance
