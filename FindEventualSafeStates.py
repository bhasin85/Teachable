class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        output = []
        for i in range(len(graph)):
            if (self._DFS(i, graph, [], "--")):
                output.append(i)
            
        return output
    
    
    def _DFS(self, i, graph, visited, prefix):
        #print("{}>{} visited:{}".format(prefix, i, visited))
        node = graph[i]
        if len(node) == 0:
            return True
        
        if i in visited:
            return False
        else:
            visited.append(i)
            
        for j in node:
            if not self._DFS(j, graph, visited[:], prefix+"--"):
                return False
            
        return True
    
