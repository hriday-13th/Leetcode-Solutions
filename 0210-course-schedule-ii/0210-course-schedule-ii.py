class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        order = []
        
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            indegree[course] += 1
            
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            node = q.popleft()
            order.append(node)
            
            for course in adj_list[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
                    
        return order if len(order) == numCourses else []