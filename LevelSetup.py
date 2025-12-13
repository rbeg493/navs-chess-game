import tkinter as tk
from Board import Board
from tkinter import Frame, Label, Tk, Canvas, YES, BOTH
import random
from pieces.Piece import Piece
from PIL import Image, ImageTk

class LevelSetup:

    def __init__(self):
        pass

    setupComplete = None
    game = None
   
    def drawBoard(self, selectedChoice, masterWindow, playerReserve, badArmy, playerArmy):
        gameBoard = Board(selectedChoice.boardHeight, selectedChoice.boardWidth, [], {}, 50, 50)
        m = tk.Toplevel(master = masterWindow)
        frame = Frame(m)
        frame.pack(expand=YES, fill=BOTH)
        self.setupComplete = tk.BooleanVar(value=False)
        

        # Board dimensions
        cellHeight = gameBoard.cellHeight
        cellWidth = gameBoard.cellWidth
        boardWidth = gameBoard.width
        boardHeight = gameBoard.height

        w = Canvas(frame, width=((boardWidth + 3) * cellWidth), height=((boardHeight + 2) * cellHeight), bg="black")
        gameBoard.canvasPaint = w
        w.pack(expand=YES, fill=BOTH)
        m.protocol("WM_DELETE_WINDOW", lambda: self.topWindowClose(m, masterWindow))

        self.placeEnemies(gameBoard, badArmy)

        # Store rectangle IDs and their positions
        rectangles = {}
        colours = {}
        w.create_rectangle(0, 0, (boardWidth + 3) * cellWidth, (boardHeight + 2) * cellHeight, fill="salmon4")
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
                colours[(row, col)] = color
        gameBoard.rectangles = rectangles
        
        # Draw enemy piece names on their positions
        for piece in badArmy:
            # Assume piece.col and piece.row are 1-based
            col = piece.col
            row = piece.row
            if 1 <= row <= boardHeight and 1 <= col <= boardWidth:
                x = col * cellWidth + cellWidth // 2
                y = row * cellHeight + cellHeight // 2
                w.create_text(x, y, text=piece.icon, fill="red", font=("Arial", 14, "bold"), tags=f"{piece.id[0]}_{piece.id[1]}")
                
        # Display player army icons to the right of the board
        self.listPlayerReserves(boardWidth, cellWidth, cellHeight, w, playerReserve)

        # Track the currently highlighted cell
        current_hover = {'cell': None}

        # Handle click to place player piece
        def on_mouse_click(event):
            col = event.x // cellWidth
            row = event.y // cellHeight
            if boardHeight - 1 <= row <= boardHeight and 1 <= col <= boardWidth:
                
                # Ensure not placing on occupied square
                occupiedSquares = [(p.row, p.col) for p in gameBoard.pieces]
                if (row, col) not in occupiedSquares:
                
                    # Loop through player reserve to find a piece to place
                    piece = playerReserve.pop(0)
                    playerArmy.append(piece)
                    piece.col = col
                    piece.row = row
                    piece.id = [row, col]

                    # Draw the icon in the clicked cell
                    x = col * cellWidth + cellWidth // 2
                    y = row * cellHeight + cellHeight // 2
                    #w.create_text(x, y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"), tags=f"{piece.id[0]}_{piece.id[1]}")

                    # Load image
                    img_path = "pawn.png"
                    img = Image.open(img_path)

                    # Resize image
                    img = img.resize((40, 40), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)

                    # Create image at center of cell (x, y)
                    w.create_image(x, y, image=photo, tags=f"{piece.id[0]}_{piece.id[1]}")

                    # Store a reference to the PhotoImage object to prevent it from being garbage collected
                    piece.img = photo



                    # Optionally, add to gameBoard.pieces
                    gameBoard.pieces.append(piece)

                    # Redraw player reserves
                    # Inefficient. Maybe optimize later.
                    w.delete("reserveList")
                    self.listPlayerReserves(boardWidth, cellWidth, cellHeight, w, playerReserve)

                    # if all pieces placed, unbind events and close window
                    if not playerReserve:
                        self.setupComplete.set(True)
                        w.unbind('<Motion>')
                        w.unbind('<Button-1>')
                        
                        # Clear cell highlight
                        prev_rect = rectangles[current_hover['cell']]
                        prev_color = colours[current_hover['cell']]
                        w.itemconfig(prev_rect, fill=prev_color)
                        current_hover['cell'] = None
                        

        def on_mouse_move(event):
            col = event.x // cellWidth
            row = event.y // cellHeight

            # enable highlighting valid board squares (last two rows for player)
            maxHeight = boardHeight - 1
            
            # Only highlight within board bounds
            if maxHeight <= row <= boardHeight and 1 <= col <= boardWidth:
                cell = (row, col)
                rect_id = rectangles.get(cell)

                # If hovering over a new cell
                if rect_id and current_hover['cell'] != cell:

                    # Restore previous cell color
                    if current_hover['cell']:
                        prev_rect = rectangles[current_hover['cell']]
                        prev_color = colours[current_hover['cell']]
                        w.itemconfig(prev_rect, fill=prev_color)

                    # Set new cell to yellow
                    w.itemconfig(rect_id, fill='yellow2')
                    current_hover['cell'] = cell
            else:
                # If not hovering over any cell, restore previous
                if current_hover['cell']:
                    prev_rect = rectangles[current_hover['cell']]
                    prev_color = colours[current_hover['cell']]
                    w.itemconfig(prev_rect, fill=prev_color)
                    current_hover['cell'] = None

        w.bind('<Motion>', on_mouse_move)
        w.bind('<Button-1>', on_mouse_click)
        return gameBoard, m, w, rectangles, colours


    def placeEnemies(self, gameBoard, badArmy):

        # Randomise enemy positions
        for piece in badArmy:
            if piece.col == 0:
                tempWidthPos = random.randint(1, gameBoard.width)
                tempHeightPos = random.randint(1, 2)

                # Ensure no two enemies occupy the same position
                while any(p.col == tempWidthPos and p.row == tempHeightPos for p in gameBoard.pieces):
                    tempWidthPos = random.randint(1, gameBoard.width)
                    tempHeightPos = random.randint(1, 2)
                piece.col = tempWidthPos
                piece.row = tempHeightPos
                piece.id = [piece.row, piece.col]
            gameBoard.pieces.append(piece)


    def listPlayerReserves(self, boardWidth, cellWidth, cellHeight, w, playerReserve):
            icon_x = (boardWidth + 1.5) * cellWidth
            icon_start_y = cellHeight
            icon_spacing = 30
            for idx, piece in enumerate(playerReserve):
                icon_y = icon_start_y + idx * icon_spacing
                w.create_text(icon_x, icon_y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"), anchor="w", tags=f"reserveList")


    def topWindowClose(self, window, masterWindow):
        window.destroy()
        masterWindow.deiconify()
        self.setupComplete.set(False)
        # update the variable waiting in the main loop (game.levelComplete)
        if self.game:
            self.game.levelComplete.set(True)

