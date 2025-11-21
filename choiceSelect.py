from Choice import Choice
import tkinter as tk
from tkinter import Frame, Label, Tk, Canvas, YES, BOTH
import random
from Board import Board
from pieces.Piece import Piece

class choiceSelect:

    choiceList = []
    selected_choice = None

    def __init__(self):
        return

    def generate_choices(self):
        choiceNum = 3
        for i in range(choiceNum):
            newChoice = Choice(random.randint(2, 4), random.randint(1, 10),5,5)
            self.choiceList.append(newChoice)

    def display_choices(self):
        w = tk.Toplevel()
        w.title("Select a Choice")
        w.geometry("600x200")

        def on_choice_click(idx):
            w.destroy()  # Close the choice window
            self.selected_choice = self.choiceList[idx]
            self.drawBoard(self.selected_choice)

        # Create a frame for each choice
        for idx, choice in enumerate(self.choiceList):
            frame = Frame(w, borderwidth=2, relief="groove", width=200, height=200)
            frame.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")
            # Make the whole frame clickable
            frame.bind("<Button-1>", lambda e, i=idx: on_choice_click(i))
            # Display choice attributes (customize as needed)
            Label(frame, text=f"Choice {idx+1}", font=("Arial", 14, "bold")).pack(pady=10)
            Label(frame, text=f"Number of Enemies: {getattr(choice, 'enemyNumber', '')}").pack()
            Label(frame, text=f"Reward ID: {getattr(choice, 'reward', '')}").pack()
            # Make labels clickable too
            for child in frame.winfo_children():
                child.bind("<Button-1>", lambda e, i=idx: on_choice_click(i))

        # Make columns expand equally
        for i in range(3):
            w.grid_columnconfigure(i, weight=1)
        w.mainloop()

    def listPlayerReserves(self, boardWidth, cellWidth, cellHeight, w, playerReserve):
        icon_x = (boardWidth + 1.5) * cellWidth
        icon_start_y = cellHeight
        icon_spacing = 30
        for idx, piece in enumerate(playerReserve):
            print(idx)
            icon_y = icon_start_y + idx * icon_spacing
            w.create_text(icon_x, icon_y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"), anchor="w", tags=f"reserveList")

        # idx = 0
        # while playerReserve:
        #     piece = playerReserve.pop(0)
        #     icon_y = icon_start_y + idx * icon_spacing
        #     w.create_text(icon_x, icon_y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"), anchor="w")
        #     idx += 1



    def drawBoard(self, selectedChoice):
        
        gameBoard = Board(selectedChoice.boardHeight, selectedChoice.boardWidth, [])
        playerArmy = []
        badArmy = []
        playerReserve = []


        # Generate enemies
        for i in range(selectedChoice.enemyNumber):
            newPiece = Piece(0, 0, "Pawn")
            badArmy.append(newPiece)

        # Randomise enemy positions
        for piece in badArmy:
            if piece.width_pos ==0:
                tempWidthPos = random.randint(1, gameBoard.width)
                tempHeightPos = random.randint(1, 2)
                # Ensure no two enemies occupy the same position
                while any(p.width_pos == tempWidthPos and p.height_pos == tempHeightPos for p in gameBoard.pieces):
                    tempWidthPos = random.randint(1, gameBoard.width)
                    tempHeightPos = random.randint(1, 2)
                piece.width_pos = tempWidthPos
                piece.height_pos = tempHeightPos
            gameBoard.pieces.append(piece)
            
        # Generate player pieces
        for i in range(3):
            newPiece = Piece(0, 0, "Pawn")
            playerReserve.append(newPiece)


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
        self.listPlayerReserves(boardWidth, cellWidth, cellHeight, w, playerReserve)

        # Track the currently highlighted cell
        current_hover = {'cell': None}

        # Handle click to place player piece
        def on_mouse_click(event):
            col = event.x // cellWidth
            row = event.y // cellHeight
            if 1 <= row <= boardHeight and 1 <= col <= boardWidth:

                # Find the next player piece with width_pos == 0
                # for piece in playerReserve:
                while playerReserve:
                    piece = playerReserve.pop(0)
                    if piece.width_pos == 0:
                        piece.width_pos = col
                        piece.height_pos = row

                        # Draw the icon in the clicked cell
                        x = col * cellWidth + cellWidth // 2
                        y = row * cellHeight + cellHeight // 2
                        w.create_text(x, y, text=piece.icon, fill="blue", font=("Arial", 14, "bold"))

                        # Optionally, add to gameBoard.pieces
                        gameBoard.pieces.append(piece)

                        # Redraw player reserves
                        w.delete("reserveList")
                        self.listPlayerReserves(boardWidth, cellWidth, cellHeight, w, playerReserve)
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

pass
