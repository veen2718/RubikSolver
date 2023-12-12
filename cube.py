from display import *

import numpy as np


def findIndex(arr,a,b):
    try:
        return arr.index(a)
    except:
        return arr.index(b)

directions = ['U','L','F','R','B','D']

touchingFaces = { #This dictionary contains information about all the faces touching a specific face. For example, the green face would correspond to [0,1,3,5] which are the indexes for white, orange, red and yellow
    
    # To Rotate a side, we take the three bottom squares on the face top of the face we are rotating and make that the leftmost column of the face to the right. Take the leftmost column of the face to the right, and make that the top squares on the face to the bottom, etc.
    # Before we do this, we cant just take, for example, the three bottom squares, as if we were trying to turn, for example, the orange face, those squares would be the three bottom squares for the green face, but not from the perspective of the orange face. So we have to rotate the faces to adjust.
    
    # Face -> Top, times Top must rotate, Left, times Left must rotate, Right, times Right must rotate, Bottom, times Bottom must rotate
    0:[4,2,1,3,2], #White -> Blue, Orange, Red, Green
    1:[0,1,4,2,5], #Orange -> White, Blue, Green, Yellow
    2:[0,0,1,3,5], #Green -> White, Orange, Red, Yellow
    3:[0,2,3,4,5], #Red -> White, Green, Blue, Yellow
    4:[0,3,2,1,5], #Blue -> White, Red, Orange, Yellow
    5:[2,1,3,4], #Yellow -> Green, Orange, Red, Blue
}

class corner:
    def __init__(self,contents):
        self.contents = list(contents)#Will be a list like ["W",0,"Green","Red",0,0]
        self.directions = []
        for direction, value in zip(directions,self.contents):
            setattr(self,direction,value)
            if value != '0':
                self.directions.append(direction)
        
        #WYdirection  = directions[findIndex(self.contents),"W","Y"]
        
class edge:
    def __init__(self,color,direction):
            self.c1 = list(color)[0]
            self.c2 = list(color)[1]
            self.d1 = list(direction)[0]
            self.d2 = list(direction)[1]

class center:
    def __init__(self,color, direction):
        self.color = color
        self.direction = direction


class layer:
    def __init__(self, edges,centers,corners=None):
        if corners:
            self.corners = [corner(x) for x in corners]
        else:
            self.corners = None
        self.edges = [edge(x[0],x[1]) for x in edges]
        print(*centers)
        self.centers = [center(*(x)) for x in centers]



class cube:
    def __init__(self):
        Corners = [
            "WOG000",
            "W0GR00",
            "W00RB0",
            "WO00B0",

            "0OG00Y",
            "00GR0Y",
            "000RBY",
            "0O00BY",
        ]

        Edges = [
            ["WO","UL"],
            ["WG","UF"],
            ["WR","UR"],
            ["WB","UB"],

            ["OG","LF"],
            ["GR","FR"],
            ["RB","RB"],
            ["BO","BL"],

            ["YO","DL"],
            ["YG","DF"],
            ["YR","DR"],
            ["YB","DB"],
        ]

        centers = [
            ["W","U"],
            ["O","L"],
            ["G","F"],
            ["R","R"],
            ["B","B"],
            ["Y","D"]
        ]

        self.layers = [
            layer(Edges[0:4],[centers[0]],Corners[0:4]),
            layer(Edges[4:8],centers[1:5]),
            layer(Edges[8:12],[centers[5]],Corners[4:8])
        ]
        


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
   
    def displayAttributes(self):
        counter = 1
        for layer in self.layers:
            print(f"Layer{counter}")
            if layer.corners:
                print(f" Corners:")
                for corner in layer.corners:
                    print(f"  {corner.contents}")
            print(" Edges")
            for edge in layer.edges:
                print(f"  {edge.c1}, {edge.c2}, {edge.d1}, {edge.d2}")
            print(" Centers")
            for center in layer.centers:
                print(f"  {center.color}, {center.direction}")

            counter += 1
            print()



x = cube()

x.displayAttributes()