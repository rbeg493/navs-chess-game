

class Piece:
    
    validMoveList = []
    # Movement capabilities
    up = 1
    down = 0
    left = 0
    right = 0
    diagDownRight = 0
    diagUpRight = 0
    diagDownLeft = 0
    diagUpLeft = 0
    
    def __init__(self, col = 0, row = 0, icon = "", color = None):
        self.col = col
        self.row = row
        self.icon = icon
        self.color = color
        self.id = [row, col]

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
        # Commented out code is possible future implementation using a single method for all directions
        # for direction in ['up', 'down', 'left', 'right']:
        #     self.checkDirection(direction, board)

        self.checkUp(board)
        self.checkDown(board)
        self.checkLeft(board)
        self.checkRight(board)
        self.checkDiagUpLeft(board)
        self.checkDiagUpRight(board)
        self.checkDiagDownLeft(board)
        self.checkDiagDownRight(board)

        for cell in self.validMoveList:
            board.canvasPaint.itemconfig(board.rectangles[(cell[0], cell[1])], fill="green")
    
    def checkUp (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.up + 1):
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


    def checkDown (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.down + 1):
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


    def checkDiagUpLeft (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.diagUpLeft + 1):
            canMove = True

            # Check if target cell diagonal down left is occupied by piece with same colour
            for piece in board.pieces:
                if piece.color == self.color:
                    if (piece.col == self.col - i and piece.row == self.row - i):
                        canMove = False
                        return
                else:
                    # Check if target cell diagonal down left is occupied by piece with different colour
                    if (piece.col == self.col - i and piece.row == self.row - i):
                        self.validMoveList.append((self.row - i, self.col - i))
                        return

            # Check if target cell diagonal down left is on the board
            if not(1 <= self.row - i <= board.height) or not(1 <= self.col - i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                self.validMoveList.append((self.row - i, self.col - i))


    def checkDiagUpRight (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.diagUpRight + 1):
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


    def checkDiagDownLeft (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.diagDownLeft + 1):
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


    def checkDiagDownRight (self, board):
        '''
        Start from piece position and tests cells in direction till max range. Valid cell rules are: Cannot occupy same colour piece, can occupy different colour piece (stops after), Cannot jump over pieces, Cannot go off board. 
        '''

        for i in range(1,self.diagDownRight + 1):
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
        
