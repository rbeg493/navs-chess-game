
from tkinter import *


class Gameplay:

    levelComplete = None
    upgradeComplete = None

    def __init__(self, playerArmy, gameBoard, badArmy):
        self.playerArmy = playerArmy
        self.gameBoard = gameBoard
        self.badArmy = badArmy
        self.pieceToMove = None

        
    def applyUpgrade(self, upgradeID, masterWindow):
        self.upgradeComplete = BooleanVar(value=False)

        # open upgrade window
        w = Toplevel()
        w.title("Apply Upgrade")
        w.geometry("600x200")
        w.protocol("WM_DELETE_WINDOW", lambda: self.topWindowClose(w, masterWindow))

        upgradeList = [
            {"id": 1, "name": "+1 Left / Right"},
            {"id": 2, "name": "+1 Up / Down"},
            {"id": 3, "name": "+1 Diagonal"}
        ]


        def on_choice_click(self, idx):
            #print(f"Upgrade applied to piece {idx}")
            #print(f"Old stats: Left {self.playerArmy[idx].left}, Right {self.playerArmy[idx].right}, Up {self.playerArmy[idx].up}, Down {self.playerArmy[idx].down}, Diagonal down right {self.playerArmy[idx].diagDownRight}, Diagonal up right {self.playerArmy[idx].diagUpRight}, Diagonal down left {self.playerArmy[idx].diagDownLeft}, Diagonal up left {self.playerArmy[idx].diagUpLeft}")

            #apply upgrade to selected piece
            if upgradeID == 1:
                self.playerArmy[idx].right += 1
                self.playerArmy[idx].left += 1
            elif upgradeID == 2:
                self.playerArmy[idx].up += 1
                self.playerArmy[idx].down += 1
            elif upgradeID == 3:
                self.playerArmy[idx].diagDownRight += 1
                self.playerArmy[idx].diagUpRight += 1
                self.playerArmy[idx].diagDownLeft += 1
                self.playerArmy[idx].diagUpLeft += 1
            #print(f"New stats: Left {self.playerArmy[idx].left}, Right {self.playerArmy[idx].right}, Up {self.playerArmy[idx].up}, Down {self.playerArmy[idx].down}, Diagonal down right {self.playerArmy[idx].diagDownRight}, Diagonal up right {self.playerArmy[idx].diagUpRight}, Diagonal down left {self.playerArmy[idx].diagDownLeft}, Diagonal up left {self.playerArmy[idx].diagUpLeft}")

            # Close the choice window
            w.destroy()  

            # go back to main menu?
            self.upgradeComplete.set(TRUE)
            #masterWindow.deiconify()


        #display upgrade at the top
        content = Frame(w)
        frame = Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
        namelbl = Label(content, text=f"upgrade: {upgradeList[upgradeID - 1]['name']}")

        content.grid(column=0, row=0)
        namelbl.grid(column=0, row=0)
        frame.grid(column=0, row=1, columnspan=3, rowspan=2)

        #let player select a piece to upgrade
        for idx, piece in enumerate(self.playerArmy):
            
            # Display piece selection
            buttonList=[]

            # Display a button for each piece that runs
            for piece in self.playerArmy:
                newButton = Button(frame, text=f"Piece {idx+1}", command=lambda i=idx: on_choice_click(self, i))
                newButton.grid(column=idx+1, row=1)
                buttonList.append(newButton)

    def topWindowClose(self, window, masterWindow):
        window.destroy()
        masterWindow.deiconify()


    def playGame(self, m, w, rectangles, colours, selectedChoice):

        self.levelComplete = BooleanVar(value=False)
        
        # Track the currently highlighted cell
        current_hover = {'cell': None}

        # Handle click to place player piece
        def on_mouse_click(event):
            col = event.x // self.gameBoard.cellWidth
            row = event.y // self.gameBoard.cellHeight
            if self.pieceToMove:
                
                # Check if clicked cell is a valid move
                if not self.pieceToMove.isValidMove(row, col, self.gameBoard):
                    self.pieceToMove.clearHighlights(self.gameBoard, colours)
                    self.pieceToMove.validMoveList.clear()
                    self.pieceToMove = None
                    return

                # Delete old piece
                w.delete(f"{self.pieceToMove.id[0]}_{self.pieceToMove.id[1]}")

                # Delete any piece at the target location (capture)
                w.delete(f"{row}_{col}")
                enemyCheck = self.gameBoard.getPieceAt(row, col)
                if enemyCheck:
                    self.gameBoard.pieces.remove(enemyCheck)
                    self.badArmy.remove(enemyCheck)
                    
                
                # Move the selected piece to the new location
                self.pieceToMove.col = col
                self.pieceToMove.row = row
                self.pieceToMove.id = [row, col]

                # Draw the icon in the clicked cell
                x = col * self.gameBoard.cellWidth + self.gameBoard.cellWidth // 2
                y = row * self.gameBoard.cellHeight + self.gameBoard.cellHeight // 2
                w.create_text(x, y, text=self.pieceToMove.icon, fill="blue", font=("Arial", 14, "bold"), tags=f"{self.pieceToMove.id[0]}_{self.pieceToMove.id[1]}")
                
                # clear highlights
                self.pieceToMove.clearHighlights(self.gameBoard, colours)
                self.pieceToMove.validMoveList.clear()

                # Reset piece to move
                self.pieceToMove = None

                # Check if level is finished
                if not self.badArmy or not self.playerArmy:
                    
                    w.unbind('<Motion>')
                    w.unbind('<Button-1>')
                    self.applyUpgrade(selectedChoice.reward, m)
                    m.master.wait_variable(self.upgradeComplete)
                    m.destroy()
                    self.levelComplete.set(True)

            else:
                # Select piece to move if clicked on own piece
                for piece in self.playerArmy:
                    if piece.col == col and piece.row == row:
                        self.pieceToMove = piece

                        # Highlight valid moves
                        piece.highlightMoves(self.gameBoard)
                        break


        def on_mouse_move(event):
                if not self.pieceToMove:
                    col = event.x // self.gameBoard.cellWidth
                    row = event.y // self.gameBoard.cellHeight

                    #enable highlighting any square
                    maxHeight = 1

                    # Only highlight within board bounds
                    if maxHeight <= row <= self.gameBoard.height and 1 <= col <= self.gameBoard.width:
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


       
