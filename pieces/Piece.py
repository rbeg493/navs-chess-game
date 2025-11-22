

class Piece:
    color = None

    # Width and height positions = col and row positions on the board
    col = 0
    row = 0
    icon = ""
    
    # Movement capabilities
    up = 1
    down = 0
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
        # Check within board
        if not(1 <= newRow <= board.height and 1 <= newCol <= board.width):
            return False
        # Check for same color piece in target
        for piece in board.pieces:
            if piece.color == self.color and piece.col == newCol and piece.row == newRow:
                return False
        
        

        return True
    
    def highlightMoves(self, board):
        #Checks for if target is in movement range
        
        #start from piece position and test each direction till max range
        #does target contain a piece of same colour
        #does target contain piece of other colour
        #is target on map

        # Check up
        for i in range(1,self.up+1):
            # Check if occupied by piece with same colour

            board.canvasPaint.itemconfig(board.rectangles[(self.row - i, self.col)], fill="green")

        # Check down
        for i in range(1,self.down+1):
            board.canvasPaint.itemconfig(board.rectangles[(self.row+i, self.col)], fill="green")

        # Check left
        for i in range(1,self.left+1):
            board.canvasPaint.itemconfig(board.rectangles[(self.col-i, self.row)], fill="green")
        
        # Check down
        for i in range(1,self.right+1):
            board.canvasPaint.itemconfig(board.rectangles[(self.col+i, self.row)], fill="green")

    


