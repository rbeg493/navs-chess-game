class Board:
    canvasPaint = None
    def __init__(self, boardWidth, boardHeight, pieces, rectangles, cellWidth = 50, cellHeight = 50):
        self.width = boardWidth
        self.height = boardHeight
        self.pieces = pieces
        self.rectangles = rectangles
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight

    def getPieceAt(self, row, col):
        for piece in self.pieces:
            if piece.row == row and piece.col == col:
                return piece
        return None

    
