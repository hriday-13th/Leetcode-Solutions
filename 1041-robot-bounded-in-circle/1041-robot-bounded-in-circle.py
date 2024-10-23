class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        curr_dir = 0
        
        for cmd in instructions:
            if cmd == "L":
                curr_dir = (curr_dir - 1) % 4
            elif cmd == "R":
                curr_dir = (curr_dir + 1) % 4
            elif cmd == "G":
                if curr_dir == 0:
                    y += 1
                elif curr_dir == 1:
                    x += 1
                elif curr_dir == 2:
                    y -= 1
                elif curr_dir == 3:
                    x -= 1
                    
        return (x, y) == (0, 0) or curr_dir != 0
#         final_angle = math.degrees(math.atan(x / y)) if y != 0 else 0
#         dir_angle = 90 * curr_dir
        
#         buffer_angle = abs(final_angle - dir_angle)
        
#         if (x == 0 and y == 0) or ((x == 0 or y == 0) and dir_angle != 0) or buffer_angle > 90:
#             return True
        
#         return False