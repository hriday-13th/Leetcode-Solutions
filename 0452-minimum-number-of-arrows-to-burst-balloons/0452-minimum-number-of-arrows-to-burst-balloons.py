class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        overlap = [points[0]]
        
        for i in range(1, len(points)):
            if overlap[-1][0] <= points[i][0] <= overlap[-1][1] or overlap[-1][0] <= points[i][1] <= overlap[-1][1]:
                overlap[-1][1] = min(overlap[-1][1], points[i][1])
                
            else:
                overlap.append(points[i])
                
        return len(overlap)