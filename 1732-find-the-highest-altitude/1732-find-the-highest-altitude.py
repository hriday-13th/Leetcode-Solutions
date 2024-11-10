class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        heights = [0]
        
        for i in gain:
            heights.append(heights[-1] + i)
            
        return max(heights)