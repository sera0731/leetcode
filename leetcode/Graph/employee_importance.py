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
        
        hmap = {e.id: e for e in employees}
        
        result = hmap[id].importance
        stack = [id]
        
        while stack :
            
            curr = stack.pop()
            
            for subordinate in hmap[curr].subordinates :
                result += hmap[subordinate].importance
                stack.append(subordinate)
            
        return result
        
