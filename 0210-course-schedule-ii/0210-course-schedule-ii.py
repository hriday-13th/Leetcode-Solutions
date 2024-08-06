class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degree[course] += 1
            
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
                
        order = []
        
        while q:
            node = q.popleft()
            order.append(node)
            
            for course in adj_list[node]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    q.append(course)
                    
        return order if len(order) == numCourses else []