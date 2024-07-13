class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(i)
            else:
                while stack and asteroids[stack[-1]] > 0 and asteroids[i] != 0:
                    if asteroids[stack[-1]] > abs(asteroids[i]):
                        asteroids[i] = 0
                    elif asteroids[stack[-1]] < abs(asteroids[i]):
                        asteroids[stack.pop()] = 0
                    else:
                        asteroids[i] = 0
                        asteroids[stack.pop()] = 0
                        
        return [i for i in asteroids if i != 0]