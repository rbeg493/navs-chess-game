

class Piece:
    color = None

    # Width and height positions = col and row positions on the board
    col = 0
    row = 0
    icon = ""
    
    # Movement capabilities
    up = 2
    down = 1
    left = 0
    right = 0
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
        return
        
        

        return True
    
    def highlightMoves(self, board):
        #Checks for if target is in movement range
        
        #start from piece position and test each direction till max range
        #does target contain a piece of same colour
        #does target contain piece of other colour
        #is target on map

        # Check up
        for i in range(1,self.up+1):
            canMove = True

            # Check if occupied by piece with same colour
            for piece in board.pieces:
                if canMove == True and piece.col == self.col and piece.row == self.row - i and piece.color == self.color:
                    canMove = False

            # Check if target is on the board
            if not(1 <= self.row - i <= board.height):
                canMove = False
                
            # Highlight if valid
            if canMove == True:
                board.canvasPaint.itemconfig(board.rectangles[(self.row - i, self.col)], fill="green")

        # Check down
        for i in range(1,self.down+1):
            canMove = True

            # Check if occupied by piece with same colour
            for piece in board.pieces:                
                if canMove == True and piece.col == self.col and piece.row == self.row+i and piece.color == self.color:
                    canMove = False

            # Check if target is on the board
            if not(1 <= self.row + i <= board.height):
                canMove = False
                
            # Highlight if valid
            if canMove == True:
                board.canvasPaint.itemconfig(board.rectangles[(self.row + i, self.col)], fill="green")

        # Check left
        for i in range(1,self.left+1):
            canMove = True

            # Check if occupied by piece with same colour
            for piece in board.pieces:                
                if canMove == True and piece.col == self.col - i and piece.row == self.row and piece.color == self.color:
                    canMove = False

            # Check if target is on the board
            if not(1 <= self.col -i <= board.height):
                canMove = False
                
            # Highlight if valid
            if canMove == True:
                board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col-i)], fill="green")
        
        # Check down
        for i in range(1,self.right+1):
            canMove = True

            # Check if occupied by piece with same colour
            for piece in board.pieces:                
                if canMove == True and piece.col == self.col + i and piece.row == self.row and piece.color == self.color:
                    canMove = False

            # Check if target is on the board
            if not(1 <= self.col +i <= board.height):
                canMove = False
                
            # Highlight if valid
            if canMove == True:
                board.canvasPaint.itemconfig(board.rectangles[(self.row, self.col+i)], fill="green")

    


