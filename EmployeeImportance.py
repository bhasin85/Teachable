"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance_list = {}
        subordinates_list = {}
        
        for employee in employees:
            importance_list[employee.id] = employee.importance
            subordinates_list[employee.id] = employee.subordinates 
            
        #print("importance_list {}".format(importance_list))
        #print("subordinates_list {}".format(subordinates_list))
        
        return self._getImportance(subordinates_list, importance_list, id)
    
    def _getImportance(self, subordinates_list, importance_list, id) -> int:
        #print("Looking for importance of {}".format(id))
        total_importance = importance_list[id]
        for subordinate_id in subordinates_list[id]:
            total_importance += self._getImportance(subordinates_list, importance_list, subordinate_id)
            
        return total_importance
