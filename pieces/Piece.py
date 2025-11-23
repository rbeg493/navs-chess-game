

class Piece:
    color = None

    # Width and height positions = col and row positions on the board
    col = 0
    row = 0
    icon = ""
    
    # Movement capabilities
    up = 3
    down = 3
    left = 3
    right = 3
    diag = 0
    
    id = [row, col]

    
    
    def __init__(self, col, row, icon, color):
        self.col = col
        self.row = row
        self.icon = icon
        self.color = color

    def __str__(self):
        return f"Color: {self.color},id: {self.id},icon: {self.icon}"
    
    def isValidMove(self, newRow, newCol, board):
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
                        board.canvasPaint.itemconfig(board.rectangles[(self.row - i, self.col)], fill="green")
                        return

            # Check if target cell up is on the board
            if not(1 <= self.row - i <= board.height):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                board.canvasPaint.itemconfig(board.rectangles[(self.row - i, self.col)], fill="green")


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
                        board.canvasPaint.itemconfig(board.rectangles[(self.row + i, self.col)], fill="green")
                        return

            # Check if target cell down is on the board
            if not(1 <= self.row + i <= board.height):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                board.canvasPaint.itemconfig(board.rectangles[(self.row + i, self.col)], fill="green")


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
                        board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col + i)], fill="green")
                        return

            # Check if target cell right is on the board
            if not(1 <= self.col + i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col + i)], fill="green")


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
                        board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col - i)], fill="green")
                        return

            # Check if target cell left is on the board
            if not(1 <= self.col - i <= board.width):
                canMove = False
                
            # Highlight cell if valid
            if canMove == True:
                board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col - i)], fill="green")


    