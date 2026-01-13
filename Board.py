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
        for pieceID in self.pieces:
            piece = self.pieces[pieceID]
            if piece.row == row and piece.col == col:
                return pieceID
        return None

    
