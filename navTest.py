
from pieces import *
from Board import *
from tkinter import *
import random


gameBoard = Board(4, 4, [])
playerArmy = []
badArmy = []


# Generate enemies
newPiece = Piece(0, 0, "Pawn")
badArmy.append(newPiece)

# Randomise enemy positions
for piece in badArmy:
    if piece.width_pos ==0:
        piece.width_pos = random.randint(1, gameBoard.width)
        # Only spawn in first two rows
        piece.height_pos = random.randint(1, 2)
    gameBoard.pieces.append(piece)
    
# Generate player pieces
for i in range(3):
    newPiece = Piece(0, 0, "Pawn")
    playerArmy.append(newPiece)


m = Tk()
frame = Frame(m)
frame.pack(expand=YES, fill=BOTH)

cellHeight = 50
cellWidth = 50
boardWidth = gameBoard.width
boardHeight = gameBoard.height

w = Canvas(frame, width=((boardWidth + 2) * cellWidth), height=((boardHeight + 2) * cellHeight), bg="black")
w.pack(expand=YES, fill=BOTH)


# Store rectangle IDs and their positions
rectangles = {}
colors = {}
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
        rect_id = w.create_rectangle(x1, y1, x2, y2, fill=color, tags=f"cell_{row}_{col}")
        rectangles[(row, col)] = rect_id
        colors[(row, col)] = color

# Draw enemy piece names on their positions
for piece in badArmy:
    # Assume piece.width_pos and piece.height_pos are 1-based
    col = piece.width_pos
    row = piece.height_pos
    if 1 <= row <= boardHeight and 1 <= col <= boardWidth:
        x = col * cellWidth + cellWidth // 2
        y = row * cellHeight + cellHeight // 2
        w.create_text(x, y, text=piece.icon, fill="red", font=("Arial", 14, "bold"))

# Display player army icons to the right of the board
icon_x = (boardWidth + 1.5) * cellWidth
icon_start_y = cellHeight
icon_spacing = 30
for idx, piece in enumerate(playerArmy):
    icon_y = icon_start_y + idx * icon_spacing
    w.create_text(icon_x, icon_y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"), anchor="w")

# Track the currently highlighted cell
current_hover = {'cell': None}

# Handle click to place player piece
def on_mouse_click(event):
    col = event.x // cellWidth
    row = event.y // cellHeight
    if 1 <= row <= boardHeight and 1 <= col <= boardWidth:
        # Find the next player piece with width_pos == 0
        for piece in playerArmy:
            if piece.width_pos == 0:
                piece.width_pos = col
                piece.height_pos = row
                # Draw the icon in the clicked cell
                x = col * cellWidth + cellWidth // 2
                y = row * cellHeight + cellHeight // 2
                w.create_text(x, y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"))
                # Optionally, add to gameBoard.pieces
                gameBoard.pieces.append(piece)
                break

def on_mouse_move(event):
    col = event.x // cellWidth
    row = event.y // cellHeight
    # Only highlight valid board squares
    if 1 <= row <= boardHeight and 1 <= col <= boardWidth:
        cell = (row, col)
        rect_id = rectangles.get(cell)
        if rect_id:
            # If hovering over a new cell
            if current_hover['cell'] != cell:
                # Restore previous cell color
                if current_hover['cell']:
                    prev_rect = rectangles[current_hover['cell']]
                    prev_color = colors[current_hover['cell']]
                    w.itemconfig(prev_rect, fill=prev_color)
                # Set new cell to yellow
                w.itemconfig(rect_id, fill='yellow')
                current_hover['cell'] = cell
    else:
        # If not hovering over any cell, restore previous
        if current_hover['cell']:
            prev_rect = rectangles[current_hover['cell']]
            prev_color = colors[current_hover['cell']]
            w.itemconfig(prev_rect, fill=prev_color)
            current_hover['cell'] = None

w.bind('<Motion>', on_mouse_move)
w.bind('<Button-1>', on_mouse_click)

#Run the window
m.mainloop()