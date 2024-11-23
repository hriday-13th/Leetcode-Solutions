class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        for i in range(rows):
            empty = cols - 1
            for j in range(cols - 1, -1, -1):
                if box[i][j] == '#':
                    box[i][j], box[i][empty] = '.', '#'
                    empty -= 1
                elif box[i][j] == '*':
                    empty = j - 1
        return [[box[rows - 1 - i][j] for i in range(rows)] for j in range(cols)]