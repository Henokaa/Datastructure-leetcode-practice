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
                
        def dfs(id):
            imp = emps[id].importance            
            for s in emps[id].subordinates:
                imp += dfs(s)
            return imp
        emps= {emp.id: emp for emp in employees}
        print(emps)
        return dfs(id)
        

        
        