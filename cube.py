from display import *

import numpy as np

touchingFaces = { #This dictionary contains information about all the faces touching a specific face. For example, the green face would correspond to [0,1,3,5] which are the indexes for white, orange, red and yellow
    # Face -> Top, Left, Right, Bottom
    0:[4,1,3,2], #White -> Blue, Orange, Red, Green
    1:[0,4,2,5], #Orange -> White, Blue, Green, Yellow
    2:[0,1,3,5], #Green -> White, Orange, Red, Yellow
    3:[0,2,4,5], #Red -> White, Green, Blue, Yellow
    4:[0,3,1,5], #Blue -> White, Red, Orange, Yellow
    5:[]
}


class cube:
    def __init__(self):
        self.contents = [
            [["W" for _ in range(3)] for _ in range(3)],
            [["O" for _ in range(3)] for _ in range(3)],
            [["G" for _ in range(3)] for _ in range(3)],
            [["R" for _ in range(3)] for _ in range(3)],
            [["B" for _ in range(3)] for _ in range(3)],
            [["Y" for _ in range(3)] for _ in range(3)],
        ]
        self.contents[2][0][1] = "R"

    def npArray(self):
        return[np.array(face) for face in self.contents]
    def F(self):
        np_face = np.array(self.contents[2])
        rotated_cube = np.rot90(np_face)
        self.contents[2] = rotated_cube.tolist()
    
    def draw(self):
        w = self.contents[0]
        drawFace(squareSize*3 + 2*squareGap, squareGap, w, canvas)
        for i in range(4):
            drawFace(squareSize*i*3 + squareGap*(i+1), squareGap*2 + squareSize*3, self.contents[i+1], canvas)
        drawFace(squareSize*3 + 2*squareGap, 2*squareSize*3 + 3*squareGap, self.contents[5],canvas)