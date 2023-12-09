
import tkinter as tk

squareSize = 50
squareGap = 20

cWidth = 12*squareSize + 5*squareGap
cHeight = 9*squareSize + 4*squareGap

root = tk.Tk()

canvas = tk.Canvas(root,width=cWidth,height=cHeight)
print(cWidth, cHeight)

canvas.pack()

#canvas.create_rectangle(50,50,100,100,fill='blue')

def drawFace(x,y,face,canvas):
    colors = {
        "W":'white',
        "B":'blue',
        "O":'orange',
        "G":'green',
        "Y":'yellow',
        "R":'red',
    }
    for i in range(3):
        for j in range(3):
            col = colors[face[j][i]]
            x1 = x + (i) * squareSize
            x2 = x1 + squareSize
            y1 = y + (j) * squareSize
            y2 = y1 + squareSize
            canvas.create_rectangle(x1,y1,x2,y2,fill=col)
    print(x1,x2,y1,y2,col)



def doMainLoop():
    root.mainloop()

