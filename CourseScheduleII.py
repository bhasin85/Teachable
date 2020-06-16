# topological_sort 
#--> 0 return False
#----> 1 return False
#------> 0 return False
# visited 0 1
# stack
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependency_matrix = self.dependency_matrix(numCourses, prerequisites)
        #print("dependency_matrix: {}".format(dependency_matrix))
        visited = []
        stack = []
        
        for course in range(numCourses):
            #visited.append(course)
            if course not in stack:
                self.topological_sort(course, dependency_matrix, visited, stack, "--")
           
        if len(stack) == numCourses:
            return stack
        else:
            return []

    def topological_sort(self, course, dependency_matrix, visited, stack, prefix):
        if course in stack:
            return True
        
        if course not in visited:
            visited.append(course) 
        else:
            return False
        
        #print("{}>{}    stack:{} visited:{}".format(prefix, course, stack, visited))
        for dependent_course in dependency_matrix[course]:
            if not self.topological_sort(dependent_course, dependency_matrix, visited, stack, "--" + prefix):
                return False
           
        stack.append(course)
        #print("Updated stack:{}".format(stack))     
        return True
        
    def dependency_matrix(self, numCourses, prerequisites):
        dependency_matrix = [[] for _ in range(numCourses)]
        
        for prerequisite in prerequisites:
            first, second = prerequisite[0], prerequisite[1]
            dependency_matrix[first].append(second)
            
        return dependency_matrix
        
