import tkinter as tk
from Board import Board
from tkinter import Frame, Label, Tk, Canvas, YES, BOTH
import random
from pieces.Piece import Piece


class LevelSetup:

    pieceToMove = None
    playerArmy = []
    badArmy = []

    def drawBoard(self, selectedChoice, masterWindow):
        gameBoard = Board(selectedChoice.boardHeight, selectedChoice.boardWidth, [], {})
        playerReserve = []
        m = tk.Toplevel()
        frame = Frame(m)
        frame.pack(expand=YES, fill=BOTH)

        # Board dimensions
        cellHeight = 50
        cellWidth = 50
        boardWidth = gameBoard.width
        boardHeight = gameBoard.height

        w = Canvas(frame, width=((boardWidth + 3) * cellWidth), height=((boardHeight + 2) * cellHeight), bg="black")
        gameBoard.canvasPaint = w
        w.pack(expand=YES, fill=BOTH)
        m.protocol("WM_DELETE_WINDOW", lambda: self.topWindowClose(m, masterWindow))

        self.generateEnemies(self, gameBoard, selectedChoice)
        self.generatePlayerPieces(self, playerReserve)

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
        for piece in self.badArmy:
            # Assume piece.col and piece.row are 1-based
            col = piece.col
            row = piece.row
            if 1 <= row <= boardHeight and 1 <= col <= boardWidth:
                x = col * cellWidth + cellWidth // 2
                y = row * cellHeight + cellHeight // 2
                w.create_text(x, y, text=piece.icon, fill="red", font=("Arial", 14, "bold"), tags=f"{piece.id[0]}_{piece.id[1]}")
                
        # Display player army icons to the right of the board
        self.listPlayerReserves(self, boardWidth, cellWidth, cellHeight, w, playerReserve)

        # Track the currently highlighted cell
        current_hover = {'cell': None}

        # Handle click to place player piece
        def on_mouse_click(event):
            col = event.x // cellWidth
            row = event.y // cellHeight
            if playerReserve:
                if boardHeight - 1 <= row <= boardHeight and 1 <= col <= boardWidth:
                    
                    # Ensure not placing on occupied square
                    occupiedSquares = [(p.row, p.col) for p in gameBoard.pieces]
                    if (row, col) not in occupiedSquares:
                    
                        # Loop through player reserve to find a piece to place
                        piece = playerReserve.pop(0)
                        self.playerArmy.append(piece)
                        piece.col = col
                        piece.row = row
                        piece.id = [row, col]

                        # Draw the icon in the clicked cell
                        x = col * cellWidth + cellWidth // 2
                        y = row * cellHeight + cellHeight // 2
                        w.create_text(x, y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"), tags=f"{piece.id[0]}_{piece.id[1]}")

                        # Optionally, add to gameBoard.pieces
                        gameBoard.pieces.append(piece)

                        # Redraw player reserves
                        # Inefficient. Maybe optimize later.
                        w.delete("reserveList")
                        self.listPlayerReserves(self, boardWidth, cellWidth, cellHeight, w, playerReserve)
                    
            elif self.pieceToMove:
                
                # Check if clicked cell is a valid move
                if not self.pieceToMove.isValidMove(row, col, gameBoard):
                    self.pieceToMove.clearHighlights(gameBoard, colours)
                    self.pieceToMove.validMoveList.clear()
                    self.pieceToMove = None
                    return

                # Delete old piece
                w.delete(f"{self.pieceToMove.id[0]}_{self.pieceToMove.id[1]}")

                # Delete any piece at the target location (capture)
                w.delete(f"{row}_{col}")
                enemyCheck = gameBoard.getPieceAt(row, col)
                if enemyCheck:
                    gameBoard.pieces.remove(enemyCheck)
                    self.badArmy.remove(enemyCheck)
                
                # Move the selected piece to the new location
                self.pieceToMove.col = col
                self.pieceToMove.row = row
                self.pieceToMove.id = [row, col]

                # Draw the icon in the clicked cell
                x = col * cellWidth + cellWidth // 2
                y = row * cellHeight + cellHeight // 2
                w.create_text(x, y, text=self.pieceToMove.icon, fill="blue", font=("Arial", 14, "bold"), tags=f"{self.pieceToMove.id[0]}_{self.pieceToMove.id[1]}")
                
                # clear highlights
                self.pieceToMove.clearHighlights(gameBoard, colours)
                self.pieceToMove.validMoveList.clear()

                # Reset piece to move
                self.pieceToMove = None

            else:
                # Select piece to move if clicked on own piece
                for piece in self.playerArmy:
                    if piece.col == col and piece.row == row:
                        self.pieceToMove = piece

                        # Highlight valid moves
                        piece.highlightMoves(gameBoard)
                        break

        def on_mouse_move(event):
            col = event.x // cellWidth
            row = event.y // cellHeight

            # enable highlighting valid board squares (last two rows for player)
            if playerReserve:
                maxHeight = boardHeight - 1
            else:
                #enable highlighting any square
                maxHeight = 1

            # Disable highlighting if moving a piece
            if self.pieceToMove:
                return
            
            if maxHeight <= row <= boardHeight and 1 <= col <= boardWidth:
                cell = (row, col)
                rect_id = rectangles.get(cell)
                if rect_id:
                    # If hovering over a new cell
                    if current_hover['cell'] != cell:
                        # Restore previous cell color
                        if current_hover['cell']:
                            prev_rect = rectangles[current_hover['cell']]
                            prev_color = colours[current_hover['cell']]
                            w.itemconfig(prev_rect, fill=prev_color)
                        # Set new cell to yellow
                        w.itemconfig(rect_id, fill='yellow')
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

        #Run the window
        m.mainloop()


    def generateEnemies(self, gameBoard, selectedChoice):

        # Clear existing enemies
        self.badArmy.clear()

        # Generate enemies
        for i in range(selectedChoice.enemyNumber):
            newPiece = Piece(0, 0, "Pawn", "red")
            self.badArmy.append(newPiece)

        # Randomise enemy positions
        for piece in self.badArmy:
            if piece.col ==0:
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


    def generatePlayerPieces(self, playerReserve):
        for i in range(3):
            newPiece = Piece(0, 0, "Pawn", "blue")
            playerReserve.append(newPiece)


    def listPlayerReserves(self, boardWidth, cellWidth, cellHeight, w, playerReserve):
            icon_x = (boardWidth + 1.5) * cellWidth
            icon_start_y = cellHeight
            icon_spacing = 30
            for idx, piece in enumerate(playerReserve):
                icon_y = icon_start_y + idx * icon_spacing
                w.create_text(icon_x, icon_y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"), anchor="w", tags=f"reserveList")


    def topWindowClose(window, masterWindow):
        window.destroy()
        masterWindow.deiconify()