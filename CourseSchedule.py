class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = {}
        dependency_matrix = self.dependency_matrix(prerequisites, numCourses)
        print("dependency_matrix:{}".format(dependency_matrix))
        
        for course in dependency_matrix:
            if not self.complete_DFS(course, dependency_matrix, visited, []):
                return False
            
        return True
    
    
    def complete_DFS(self, course, dependency_matrix, visited, path):
        if course in visited:
            return visited[course]
        
        if course in path:
            visited[course] = False
            return False
        
        path.append(course)
        
        for dependency in dependency_matrix[course]:
            if not self.complete_DFS(dependency, dependency_matrix, visited, path):
                visited[dependency] = False
                return False  
            
        visited[course] = True
        return True
        
    def dependency_matrix(self, prerequisites, numCourses):
        dependency_matrix = {}
        
        for course in range(numCourses):
            dependency_matrix[course] = []
            
        for prerequisite in prerequisites:
            course, pre = prerequisite[0], prerequisite[1]
            if course in dependency_matrix:
                dependency_matrix[course].append(pre)
                
        return dependency_matrix
        
