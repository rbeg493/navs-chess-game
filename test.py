
from pieces.Piece import Piece
from pieces.Rook import Rook
from pieces.Pawn import Pawn
from tkinter import *

rook = Rook("Black", True)
pawn = Pawn("White", True)

m = Tk()
frame = Frame(m)
frame.pack(expand=YES, fill=BOTH)

cellHeight = 50
cellWidth = 50
boardWidth = 8
boardHeight = 8

w = Canvas(frame, width=((boardWidth + 2) * cellWidth), height=((boardHeight + 2) * cellHeight), bg="black")
w.pack(expand=YES, fill=BOTH)

w.create_rectangle(0, 0, (boardWidth + 2) * cellWidth, (boardHeight + 2) * cellHeight, fill="saddlebrown")
for row in range(1, boardHeight+1):
    for col in range(1, boardWidth+1):
        x1 = col * cellWidth
        y1 = row * cellHeight
        x2 = x1 + cellWidth
        y2 = y1 + cellHeight
        if (row + col) % 2 == 0:
            color = "white"
        else:
            color = "gray"
        w.create_rectangle(x1, y1, x2, y2, fill=color)

#Run the window
m.mainloop()