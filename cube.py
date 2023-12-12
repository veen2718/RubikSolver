from display import *

import numpy as np

touchingFaces = { #This dictionary contains information about all the faces touching a specific face. For example, the green face would correspond to [0,1,3,5] which are the indexes for white, orange, red and yellow
    
    # To Rotate a side, we take the three bottom squares on the face top of the face we are rotating and make that the leftmost column of the face to the right. Take the leftmost column of the face to the right, and make that the top squares on the face to the bottom, etc.
    # Before we do this, we cant just take, for example, the three bottom squares, as if we were trying to turn, for example, the orange face, those squares would be the three bottom squares for the green face, but not from the perspective of the orange face. So we have to rotate the faces to adjust.
    
    # Face -> Top, times Top must rotate, Left, times Left must rotate, Right, times Right must rotate, Bottom, times Bottom must rotate
    0:[4,1,3,2], #White -> Blue, Orange, Red, Green
    1:[0,3,4,2,5], #Orange -> White, Blue, Green, Yellow
    2:[0,1,3,5], #Green -> White, Orange, Red, Yellow
    3:[0,2,4,5], #Red -> White, Green, Blue, Yellow
    4:[0,3,1,5], #Blue -> White, Red, Orange, Yellow
    5:[2,1,3,4], #Yellow -> Green, Orange, Red, Blue
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
    

    def rotateFace(self, face):
        npContents = self.npArray()
        npContents[face] = np.rot90(npContents[face])
        touching = touchingFaces[face]
        if face not in [0,5]:
            top = (npContents[touching[0]])

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