

class Piece:
    
    validMoveList = []
    # Movement capabilities
    forward = 1
    back = 0
    left = 0
    right = 0
    diagBackRight = 0
    diagForwardRight = 0
    diagBackLeft = 0
    diagForwardLeft = 0
    img = None
    
    def __init__(self, col = 0, row = 0, icon = "", color = None, img = None):
        self.col = col
        self.row = row
        self.icon = icon
        self.color = color
        self.id = [row, col]
        self.img  = img

    def __str__(self):
        return f"Color: {self.color},id: {self.id},icon: {self.icon}"
    
    
    def isValidMove(self, newRow, newCol, board):
        # Check if on board
        if not(1 <= newRow <= board.height and 1 <= newCol <= board.width):
            return False

        # Check if highlighted green
        fillColor = board.canvasPaint.itemcget(board.rectangles[(newRow, newCol)], "fill")
        if fillColor == "green":
            return True
        return False
        
    
    def highlightMoves(self, board):
        '''
        Highlights valid moves on the board by checking each direction
        '''

        self.checkForward(board)
        self.checkBack(board)
        self.checkLeft(board)
        self.checkRight(board)
        self.checkDiagForwardLeft(board)
        self.checkDiagForwardRight(board)
        self.checkDiagBackLeft(board)
        self.checkDiagBackRight(board)

        for cell in self.validMoveList:
            board.canvasPaint.itemconfig(board.rectangles[(cell[0], cell[1])], fill="green")
    
    def checkForward (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.forward + 1):
            canMove = True

            # Check if target cell up is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if piece.col == self.col and piece.row == self.row - i:
                        canMove = False
                        return
                else:
                    # Check if target cell up is occupied by piece with different colour
                    if piece.col == self.col and piece.row == self.row - i:
                        #board.canvasPaint.itemconfig(board.rectangles[(self.row - i, self.col)], fill="green")
                        self.validMoveList.append((self.row - i, self.col))
                        return

            # Check if target cell up is on the board
            if not(1 <= self.row - i <= board.height):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                #board.canvasPaint.itemconfig(board.rectangles[(self.row - i, self.col)], fill="green")
                self.validMoveList.append((self.row - i, self.col))


    def checkBack (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.back + 1):
            canMove = True

            # Check if target cell down is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if piece.col == self.col and piece.row == self.row + i:
                        canMove = False
                        return
                else:
                    # Check if target cell down is occupied by piece with different colour
                    if piece.col == self.col and piece.row == self.row + i:
                        #board.canvasPaint.itemconfig(board.rectangles[(self.row + i, self.col)], fill="green")
                        self.validMoveList.append((self.row + i, self.col))
                        return

            # Check if target cell down is on the board
            if not(1 <= self.row + i <= board.height):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                #board.canvasPaint.itemconfig(board.rectangles[(self.row + i, self.col)], fill="green")
                self.validMoveList.append((self.row + i, self.col))


    def checkRight (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.right + 1):
            canMove = True

            # Check if target cell right is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if piece.col == self.col + i and piece.row == self.row:
                        canMove = False
                        return
                else:
                    # Check if target cell right is occupied by piece with different colour
                    if piece.col == self.col + i and piece.row == self.row:
                        #board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col + i)], fill="green")
                        self.validMoveList.append((self.row, self.col + i))
                        return

            # Check if target cell right is on the board
            if not(1 <= self.col + i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                #board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col + i)], fill="green")
                self.validMoveList.append((self.row, self.col + i))


    def checkLeft (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.left + 1):
            canMove = True

            # Check if target cell left is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if piece.col == self.col - i and piece.row == self.row:
                        canMove = False
                        return
                else:
                    # Check if target cell left is occupied by piece with different colour
                    if piece.col == self.col - i and piece.row == self.row:
                        #board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col - i)], fill="green")
                        self.validMoveList.append((self.row, self.col - i))
                        return

            # Check if target cell left is on the board
            if not(1 <= self.col - i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                #board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col - i)], fill="green")
                self.validMoveList.append((self.row, self.col - i))


    def checkDiagForwardLeft (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.diagForwardLeft + 1):
            canMove = True

            # Check if target cell diagonal up left is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if (piece.col == self.col - i and piece.row == self.row - i):
                        canMove = False
                        return
                else:
                    # Check if target cell diagonal up left is occupied by piece with different colour
                    if (piece.col == self.col - i and piece.row == self.row - i):
                        self.validMoveList.append((self.row - i, self.col - i))
                        return

            # Check if target cell diagonal down left is on the board
            if not(1 <= self.row - i <= board.height) or not(1 <= self.col - i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                self.validMoveList.append((self.row - i, self.col - i))


    def checkDiagForwardRight (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.diagForwardRight + 1):
            canMove = True

            # Check if target cell diagonal up right is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if (piece.col == self.col + i and piece.row == self.row - i):
                        canMove = False
                        return
                else:
                    # Check if target cell diag up right is occupied by piece with different colour
                    if (piece.col == self.col + i and piece.row == self.row - i):
                        self.validMoveList.append((self.row - i, self.col + i))
                        return

            # Check if target cell diag up right is on the board
            if not(1 <= self.row - i <= board.height) or not(1 <= self.col + i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                self.validMoveList.append((self.row - i, self.col + i))


    def checkDiagBackLeft (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.diagBackLeft + 1):
            canMove = True

            # Check if target cell diagonal down left is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if (piece.col == self.col - i and piece.row == self.row + i):
                        canMove = False
                        return
                else:
                    # Check if target cell diagonal down left is occupied by piece with different colour
                    if (piece.col == self.col - i and piece.row == self.row + i):
                        self.validMoveList.append((self.row + i, self.col - i))
                        return

            # Check if target cell diagonal down left is on the board
            if not(1 <= self.row + i <= board.height) or not(1 <= self.col - i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                self.validMoveList.append((self.row + i, self.col - i))


    def checkDiagBackRight (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.diagBackRight + 1):
            canMove = True

            # Check if target cell diagonal down right is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if (piece.col == self.col + i and piece.row == self.row + i):
                        canMove = False
                        return
                else:
                    # Check if target cell diagonal down right is occupied by piece with different colour
                    if (piece.col == self.col + i and piece.row == self.row + i):
                        self.validMoveList.append((self.row + i, self.col + i))
                        return

            # Check if target cell diagonal down right is on the board
            if not(1 <= self.row + i <= board.height) or not(1 <= self.col + i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                self.validMoveList.append((self.row + i, self.col + i))


    def clearHighlights(self, board, colours):
        '''
        Clears all highlighted cells on the board
        '''
        for cell in self.validMoveList:
            prev_rect = board.rectangles[cell]
            prev_color = colours[cell]
            board.canvasPaint.itemconfig(prev_rect, fill=prev_color)


    def setBadMovement(self):
        '''
        Sets movement capabilities for enemy pieces
        '''
        self.forward *= -1
        self.back *= -1
        self.left *= -1
        self.right *= -1
        self.diagBackRight *= -1
        self.diagForwardRight *= -1
        self.diagBackLeft *= -1
        self.diagForwardLeft *= -1
        
