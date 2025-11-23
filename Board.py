class Board:
    canvasPaint = None
    def __init__(self, width, height, pieces, rectangles):
        self.width = width
        self.height = height
        self.pieces = pieces
        self.rectangles = rectangles

    def getPieceAt(self, row, col):
        for piece in self.pieces:
            if piece.row == row and piece.col == col:
                return piece
        return None

    
