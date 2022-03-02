class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for employee in employees:
            d[employee.id] = employee
        
        def finder(employee):
                sum = employee.importance
                for i in employee.subordinates:
                    sum += finder(d[i])
                return sum
        return finder(d[id])  
