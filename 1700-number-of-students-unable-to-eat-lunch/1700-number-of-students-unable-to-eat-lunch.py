class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for i in range(len(sandwiches)):
            if students == []:
                return 0
            
            step = 0
            while sandwiches[i] != students[0] and step < len(students):
                l = students.pop(0)
                students.append(l)
                step += 1
                
            if students[0] == sandwiches[i]:
                students.pop(0)
            else:
                return len(students)
        return len(students)