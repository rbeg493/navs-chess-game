

class Piece:
    color = None

    # Width and height positions = col and row positions on the board
    width_pos = 0
    height_pos = 0
    icon = ""
    
    # Movement capabilities
    up = 1
    down = 0
    left = 0
    right = 0
    diag = 0
    
    id = [height_pos, width_pos]

    
    
    def __init__(self, width_pos, height_pos, icon, color):
        self.width_pos = width_pos
        self.height_pos = height_pos
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
            if piece.color == self.color and piece.width_pos == newCol and piece.height_pos == newRow:
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
            #highlight self.height_pos-i, self.width_pos
            #get correct rectangle from rectangles list
            #set its fill to the highlight colour
            board.canvasPaint.itemconfig(board.rectangles[(self.height_pos - i, self.width_pos)], fill="green")

        # Check down
        for i in range(1,self.down+1):
            board.canvasPaint.itemconfig(board.rectangles[(self.height_pos+i, self.width_pos)], fill="green")

        # Check left
        for i in range(1,self.left+1):
            board.canvasPaint.itemconfig(board.rectangles[(self.width_pos-i, self.height_pos)], fill="green")
        
        # Check down
        for i in range(1,self.right+1):
            board.canvasPaint.itemconfig(board.rectangles[(self.width_pos+i, self.height_pos)], fill="green")

    


